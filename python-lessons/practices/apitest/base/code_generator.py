# -*- coding: utf-8 -*-
import json
import re

from base import capitalize_first, change_camel_to_under
from jinja2 import Environment, PackageLoader

Text = 'TEXT'
POSTMAN = 'POSTMAN'
CHARLES = 'CHARLES'
POSTMAN_COLLECTION = "POSTMAN_COLLECTION"

# todo refactor for code generation
class APICodeGenerator:
    def __init__(self, curl_command: object = None,
                 source_file: object = None, source_type: object = Text,
                 original_test_data: object = None, module_name: object = None) -> object:
        """

        :rtype: object
        """
        self.curl_command = curl_command
        self.source_file = source_file
        self.source_type = source_type
        self.api_definition = {}
        self.api_request_data = []
        self.module_name = module_name
        self.original_test_data = original_test_data
        self.parse_api_definition()

    def generate_codes(self):
        print("======== api codes==========")
        print(self.render_apiclient_template())
        print("======== api codes done ==========")

        print("======== api tests codes==========")
        print(self.render_apitests_template())
        print("======== api tests codes done ==========")

    def parse_api_definition(self):

        # for original test data
        if self.original_test_data is not None and len(self.original_test_data) > 0:
            self.api_definition = self.original_test_data
            if len(self.module_name) == 0:
                raise Exception("please input module name ")
            return

        # for curl
        if self.curl_command is not None and len(self.curl_command) > 0:
            if self.source_type == CHARLES:
                self.module_name = re.search(r'.me/(.*)/invoke/',
                                             re.search(r'--compressed (.*)', self.curl_command).group(1)) \
                    .group(1).upper()
            else:
                module_matcher = re.search(r'.me/(.*)/invoke/', self.curl_command)
                try:
                    self.module_name = module_matcher.group(1).upper()
                except Exception as e:
                    self.module_name = 'NOT_NAPOS'

            if self.source_type == POSTMAN:
                api_definition_matcher = re.compile(r' -d (.*)', re.S)
                result = api_definition_matcher.findall(self.curl_command)
                self.api_definition = json.loads(result[0].split('\' ')[0].replace("\'", ""))
            else:
                api_definition_matcher = re.search(r' --data-binary (.*) --', self.curl_command)
                self.api_definition = json.loads(eval(api_definition_matcher.group(1)))
            return

        # for postman collections file
        if self.source_type == POSTMAN_COLLECTION:
            with open(self.source_file, 'r') as f:
                request_data = json.loads(''.join(f.readlines()))
                self.api_request_data = request_data.get('requests')
            self.api_definition = eval(self.api_request_data[0]['rawModeData'])
            return

    def parse_test_data(self):
        raise Exception("not support yet")

    def write_api_file(self):
        raise Exception("not support yet")

    def write_api_testcase_file(self):
        raise Exception("not support yet")

    # todo need to refactor
    def render_apitests_template(self):
        template = Environment(loader=PackageLoader('base', '')).get_template("api_test_template")
        if self.original_test_data is not None:
            expected = self.original_test_data.get('respect')
        else:
            expected = {"result": [], "error": None}

        requests = []
        if len(self.api_request_data) == 0:
            requests.append({"expected": expected,
                             "params": self.api_definition.get('params')})
        else:
            for item in self.api_request_data:  # only for postman collections
                requests.append({"expected": expected, "params": eval(item['rawModeData'])['params']})
        return template.render(method=change_camel_to_under(self.api_definition.get('method')),
                               params=self.api_definition.get('params'),
                               service_cap=capitalize_first(
                                   self.api_definition.get('service')) if self.api_definition.get('service') else '',
                               method_cap=capitalize_first(
                                   self.api_definition.get('method') if self.api_definition.get('method') else ''),
                               expected=expected, requests=requests)

    def render_apiclient_template(self):
        template = Environment(loader=PackageLoader('base', '')).get_template("api_client_template")

        if self.api_definition.get('params'):
            parameter_list = ','.join("{0} = None".format(item) for item in self.api_definition.get('params'))
            parameter_pass = ','.join("{item} ={item}".format(item=item) for item in self.api_definition.get('params'))
        else:
            parameter_list = ''
            parameter_pass = ''

        return template.render(method_cap=capitalize_first(self.api_definition.get('method')),
                               module_name=self.module_name, method=self.api_definition.get('method')
                               , parameter_list=parameter_list
                               , parameter_pass=parameter_pass)
