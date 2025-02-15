from confluent_kafka import Producer
import time

# Kafka Configuration
conf = {
    'bootstrap.servers': 'localhost:9092'  # Update with your Kafka broker
}

# Initialize Producer
producer = Producer(conf)

topic = "test_topic"

# Function to send messages
def send_message(key, message):
    producer.produce(topic, key=key, value=message)
    producer.flush()  # Ensure message is sent

# Sending multiple messages
for i in range(10):
    send_message(f'key-{i}', f'Hello Kafka {i}')
    print(f'Sent: key-{i} -> Hello Kafka {i}')
    time.sleep(1)
