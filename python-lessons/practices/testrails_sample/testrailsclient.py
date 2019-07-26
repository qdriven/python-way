# -*- coding: utf-8 -*-
import base64
import json

import requests


class APIError:
    pass


class TestRailsAPI:
    def __init__(self,
                 base_url="https://testrail.domain.me/testrail/"):
        self.user = ''
        self.password = ''
        self.headers = {'Content-Type': 'application/json'}
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + "index.php?/api/v2/"
        self.add_auth()

    def get(self, uri):
        request_url = self.__url + uri
        return requests.get(url=request_url, headers=self.headers)

    def post(self, uri, data):
        return requests.post(url=self.__url + uri,
                             data=json.dumps(data), headers=self.headers)

    def add_auth(self):
        base_auth = '%s:%s' % (self.user, self.password)
        self.headers['Authorization'] = 'Basic %s' % str(
            base64.b64encode(bytes(base_auth, 'utf-8')), 'ascii')


if __name__ == '__main__':
    response = TestRailsAPI().get("get_suites/88")
    print(response.json())
