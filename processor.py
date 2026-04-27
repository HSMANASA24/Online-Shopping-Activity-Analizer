from kafka import KafkaConsumer
import json
import os
from pymongo import MongoClient

product_stats = {}

consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
collection = db["analytics"]

print("Processing started...")

for msg in consumer:
    data = msg.value
    product = data["product_id"]
    event = data["event"]

    # ✅ Update local stats
    if product not in product_stats:
        product_stats[product] = {"view": 0, "add_to_cart": 0, "purchase": 0}

    product_stats[product][event] += 1

    # ✅ Save to MongoDB
    update = {
        "$inc": {
            "views": 1 if event == "view" else 0,
            "cart": 1 if event == "add_to_cart" else 0,
            "purchase": 1 if event == "purchase" else 0
        }
    }

    collection.update_one(
        {"product_id": product},
        update,
        upsert=True
    )

    print("Updated:", product, event)

    # ✅ SAVE JSON (FIXED - INSIDE LOOP)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILE_PATH = os.path.join(BASE_DIR, "data.json")

    with open(FILE_PATH, "w") as f:
        json.dump(product_stats, f)

    # ✅ Show Top Products
    print("\n🔥 Top Products:")
    top = sorted(product_stats.items(),
                 key=lambda x: x[1]['purchase'],
                 reverse=True)

    for p, stats in top[:3]:
        print(p, "→", stats['purchase'], "purchases")