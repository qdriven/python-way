# -*- coding: utf-8 -*-
import sys

from confluent_kafka import Consumer, KafkaException, KafkaError

from kafka_example.httptraffic_mysql_sinker import save_http_traffic
from kafka_example.httptraffic_parser import HttpTraffic

conf = {
    'bootstrap.servers': '10.8.1.43:9092',
    'group.id': "httptraffic-consumer",
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'},
    #     'security.protocol': 'SASL_SSL',
    # 'sasl.mechanisms': 'SCRAM-SHA-256',
    #     'sasl.username': os.environ['CLOUDKARAFKA_USERNAME'],
    #     'sasl.password': os.environ['CLOUDKARAFKA_PASSWORD']
}
topics = ['test']


def consume_kafka_http_traffic():
    c = Consumer(**conf)
    c.subscribe(topics)
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key())))
                try:
                    http_traffic = HttpTraffic()
                    http_traffic.parse_kafka_msg(msg.value().decode('utf-8'))
                    save_http_traffic(http_traffic)
                except Exception as e:
                    print(e)
    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')
    c.close()


if __name__ == '__main__':
    consume_kafka_http_traffic()
