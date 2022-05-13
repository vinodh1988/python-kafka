from kafka import KafkaConsumer

brokers=["localhost:9092"]
topicName = "firstone"

consumer = KafkaConsumer(topicName,group_id= "first_group",
bootstrap_servers=brokers,auto_offset_reset='earliest')

for message in consumer:
    print('Topic: %s:Partion: %d Message:%s' %(message.topic,message.partition,message.value))