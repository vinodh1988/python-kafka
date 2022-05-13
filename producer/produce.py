from kafka import KafkaProducer


brokers=["localhost:9092"]
topic="firstone"

producer=KafkaProducer(bootstrap_servers=brokers)

def messageSender(message):
    producer.send(topic,message.encode('utf-8'))
