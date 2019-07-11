# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     api_model
   Description :
   Author :        patrick
   date：          2019/7/11
-------------------------------------------------
   Change Activity:
                   2019/7/11:
-------------------------------------------------
"""
__author__ = 'patrick'


class ApiModel:

    def __init__(self, tc=None):
        self.req_url = ""
        self.method = ""
        self.req_body = ""
        self.response_body = ""
        self.name = ""
        self.headers = {}
        for k, v in tc.items():
            setattr(self, k, v)


# def test_collection_to_api_model(test_collection):
#     api = ApiModel(test_collection)
#     return api


# tc = {
#     "req_url": "testing",
#     "method": "post",
#     "req_body": "body",
#     "response_body": "res_body",
#     "name": "name",
#     "headers": {}
# }
#
# api = test_collection_to_api_model(tc)
# print(api)
