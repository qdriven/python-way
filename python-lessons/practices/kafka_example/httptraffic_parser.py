# -*- coding: utf-8 -*-

class HttpTraffic:

    def __init__(self):
        self.kafka_id = None
        self.method = None
        self.url = None
        self.headers = {}
        self.request_body = None
        self.server = None
        self.port = None
        self.response_body = None

    def _parse_kafka_request(self, kafka_raw_msg):
        parsed_request = kafka_raw_msg.split("\n")
        # headers = parsed_request[0].split("\n")
        kafka_pared_msg = parsed_request[0].split(" ")
        self.kafka_id = kafka_pared_msg[1]
        parsed_method_url = parsed_request[1].split(" ")
        self.method, self.url = parsed_method_url[0], parsed_method_url[1]
        for i in range(2, len(parsed_request)):
            escaped_header = parsed_request[i].replace("\r", "")
            if len(escaped_header) > 0 and escaped_header[0] == "{":  # parse request body
                self.request_body = parsed_request[1]
                continue
            parsed_header = escaped_header.split(":")
            if len(parsed_header) > 1:
                if parsed_header[0].find("Host") >= 0:  ## parse host
                    self.server = parsed_header[1]
                    if len(parsed_header) > 2:
                        self.port = parsed_header[2]
                else:
                    self.headers[parsed_header[0]] = parsed_header[1]
        # if len(parsed_request) > 1:
        #     self.request_body = parsed_request[1]
        return self

    def _parse_kafka_response(self, kafka_raw_msg):
        parsed_response = kafka_raw_msg.split("\n")
        if parsed_response[-1][0] == "{":
            self.response_body = parsed_response[-1]
        self.kafka_id = parsed_response[0].split(" ")[1]
        return self

    def parse_kafka_msg(self, msg):
        if msg[0] == "1":
            self._parse_kafka_request(msg)
        if msg[0] == "2":
            self._parse_kafka_response(msg)
