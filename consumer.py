from confluent_kafka import Consumer

# Kafka Configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Initialize Consumer
consumer = Consumer(conf)
topic = "test_topic"
consumer.subscribe([topic])

print("Waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0)  # Poll messages from Kafka

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f"Received: {msg.key().decode()} -> {msg.value().decode()}")

except KeyboardInterrupt:
    print("\nStopping consumer...")
finally:
    consumer.close()
