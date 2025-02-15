# Kafka Python Producer Consumer

This project demonstrates how to use **Apache Kafka** with **Python** to send and receive messages using Kafka's producer and consumer APIs. This setup allows for efficient real-time data streaming between distributed applications.

## **Prerequisites**

- **Python 3.7+**
- **Apache Kafka** (installed locally)
- **Java 8+** (required for Kafka)
- **Confluent Kafka Python library**

## **Installation**

Ensure Kafka is installed and running before proceeding.

To install the required Python dependencies, run:

```bash
pip install confluent-kafka
```

## **Usage**

1. **Start Zookeeper** (Kafka requires Zookeeper to manage brokers):

   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties &
   ```

2. **Start Kafka broker** (the main Kafka service):

   ```bash
   bin/kafka-server-start.sh config/server.properties &
   ```

3. **Create a Kafka topic** (where messages will be sent and received):

   ```bash
   bin/kafka-topics.sh --create --topic test_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

   You can verify if the topic was created successfully by running:

   ```bash
   bin/kafka-topics.sh --list --bootstrap-server localhost:9092
   ```

4. **Run the producer application** to send messages to the Kafka topic:

   ```bash
   python producer.py
   ```

   The producer will generate and send messages to `test_topic`.

5. **Run the consumer application** to receive and process messages from the topic:
   ```bash
   python consumer.py
   ```
   The consumer will subscribe to `test_topic` and print received messages.
