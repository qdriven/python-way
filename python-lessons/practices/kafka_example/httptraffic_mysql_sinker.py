# -*- coding: utf-8 -*-
import json

import records

import pymysql
pymysql.install_as_MySQLdb()

db = records.Database("mysql://root:123456@10.8.1.43/data_collector")

def save_http_traffic(http_traffic):
    # find_by_kafka_id_sql = "select * from http_traffic where kafka_id = :kafka_id"
    # record = db.query(find_by_kafka_id_sql, kafka_id=http_traffic.kafka_id)
    insert_httptraffic = """
    insert http_traffic(kafka_id, request_body, http_response, method, host, url, port, headers) 
    VALUE(:kafka_id,:request_body,:http_response,:method,:host,:url,:port,:headers) 
    """
    header_json_string = json.dumps(http_traffic.headers)
    db.query(insert_httptraffic,
             kafka_id=http_traffic.kafka_id,
             request_body=http_traffic.request_body,
             http_response=http_traffic.response_body,
             method=http_traffic.method,
             host=http_traffic.server,
             url=http_traffic.url,
             port=http_traffic.port,
             headers=header_json_string)


# http_traffic = HttpTraffic()
# http_traffic.headers = {"agent": "chrome"}
# http_traffic.url = "/test"
# http_traffic.method = "GET"
# http_traffic.request_body = "{\"agent\":\"chrome\"}"
# http_traffic.http_response = "{\"agent\":\"chrome\"}"
# http_traffic.kafka_id = "dahdlfajsdlfafds"
# save_http_traffic(http_traffic)

