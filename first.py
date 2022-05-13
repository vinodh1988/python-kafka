from kafka import KafkaProducer

brokers=["localhost:9092"]
topic="firstone"

producer=KafkaProducer(bootstrap_servers=brokers)

result=producer.send(topic,b'Hey!!!! First Message from python')

metadata=result.get()
print(metadata.topic)
print(metadata.partition)