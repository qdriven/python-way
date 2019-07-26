#!/usr/bin/env python
# -*- coding: utf-8 -*-

getApplyActivity_test_data = [
    {"description": "testcase_1", "username": "alice5", "password": "eleme517517",
     "input": {"shopId": 74753461}
        , "expected": None, "env": ["alpha"]},
    {"description": "testcase_2", "username": "alice5", "password": "eleme517517",
     "input": {"shopId": 74753}, "expected": None, "env": ["alpha"]}
]

print(getApplyActivity_test_data[0].get('input'))
print(getApplyActivity_test_data[1].get('input'))

def set_dictvalue(source_dict, path_in_dict, value):
    paths = path_in_dict.split('.')
    if len(paths)==1:
        source_dict[paths[0]]=value
        return

    changed_dict = source_dict.get(paths[0])
    for item in paths[1:len(paths)-1]:
        changed_dict = changed_dict.get(item)
    changed_dict[paths[len(paths)-1]] = value

test_dict =  {"description": "testcase_2", "username": "alice5", "password": "eleme517517",
     "input": {"shopId": 74753,"nested":{
         "nested1":"test","nest2":{
             "nested3":"test"
         }
     }}, "expected": None, "env": ["alpha"]}

set_dictvalue(test_dict,"input.nested.nest2.nested3","32566")
print(test_dict)