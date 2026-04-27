from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "user-events",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='debug-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📥 Consumer started...\n")

for message in consumer:
    data = message.value

    print("Received Event:")
    print(f"User: {data['user_id']}")
    print(f"Event: {data['event']}")
    print(f"Product: {data['product_id']}")
    print("-" * 30)