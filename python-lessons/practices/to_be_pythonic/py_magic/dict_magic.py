# -*- coding: utf-8 -*-
import json

dict_magic =""" {"result":{
    "name": "test",
    "test": "name",
    "test1": ""
}}"""

dict_magic1="""{"result":"name"}"""
json_object = json.loads(dict_magic)
json_object1 = json.loads(dict_magic1)
print(type(json_object.get('result')))
print(type(json_object1.get('result')))


class FakeDict:
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def get(self, item, default=None):
        if hasattr(self, item):
            return self.__getattribute__(item)
        return default

    def __getitem__(self, item):
        if hasattr(self, item):
            return self.__getattribute__(item)
        return None

    def __setitem__(self, key, value):
        self.__setattr__(key, value)


fake_dict = FakeDict("name", "params")
print(fake_dict.get("test"))
print(fake_dict["test"])
fake_dict['test'] = "Test111"
print(fake_dict["test"])
