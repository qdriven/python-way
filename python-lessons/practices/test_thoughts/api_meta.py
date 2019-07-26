# -*- coding: utf-8 -*-

class ApiTestMeta(object):
    url=None
    method=None
    body=dict() # templates,need to render, use jinja2
    headers = {}
    test_name=None
    expected_status =[]
    variable_binds={}
    yml_parser = None

    def __init__(self):
        pass
