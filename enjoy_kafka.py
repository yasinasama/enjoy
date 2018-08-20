# -*- coding: utf-8 -*-

from kafka import KafkaConsumer, TopicPartition


'''
Get latest/earliest offset from each partition

@:param
    server:127.0.0.1:9092      
    topic:my_topic
    group_id:my_id
@:return
'''
def topic_offset(server,topic,group_id):
    consumer = KafkaConsumer(
        bootstrap_servers=server,
        group_id=group_id
    )

    for p in consumer.partitions_for_topic(topic):
        tp = TopicPartition(topic, p)
        consumer.assign([tp])
        consumer.seek_to_end(tp)
        latest_offset = consumer.position(tp)

        consumer.seek_to_beginning(tp)
        earliest_offset = consumer.position(tp)

        print("topic: %s, partition: %s, earliest: %s, latest: %s" % (
               topic, p, earliest_offset, latest_offset))

    consumer.close()

if __name__=='__main__':
    topic_offset('10.68.120.21:9092','formattedlog','cc')