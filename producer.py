from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

events = ["view", "add_to_cart", "purchase"]
products = [f"P{i}" for i in range(1, 11)]

while True:
    data = {
        "user_id": f"U{random.randint(1,100)}",
        "event": random.choice(events),
        "product_id": random.choice(products),
        "timestamp": time.time()
    }

    producer.send("user-events", data)
    print("Sent:", data)
    time.sleep(1)