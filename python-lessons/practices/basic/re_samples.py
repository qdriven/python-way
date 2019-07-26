# -*- coding: utf-8 -*-
import json

from jinja2 import Template
from jsonpath_rw import parse

test_dict = {
    "list": [
        {"update": "1234", "sublist": [{"sub1": "1234"}, {"sub1": 1234}]},
        {"update": "1234", "sublist": [{"sub1": "1234"}, {"sub1": 1234}]},
    ]}


# json_exp = parse('list')
# print(json_exp.find(test_dict))
# for item in json_exp.find(test_dict):
#     print(item.value)
#     item.value[0]["update"] = "00900"
# print(test_dict)


def set_dictvalue(source_dict, path_in_dict, value):
    paths = path_in_dict.split(".")
    if len(paths) == 1:
        try:
            source_dict.setdefault(paths[0], value)
        except Exception as e:
            raise Exception(e + "请检查要找的字段路径是否正确,字段路径是" + path_in_dict)
    try:
        exp = parse(".".join(paths[:len(paths) - 1]))
        matched_items = exp.find(source_dict)
        for item in matched_items:
            item.value[paths[len(paths) - 1]] = value
    except Exception as e:
        raise Exception(e + "请检查要找的字段路径是否正确,字段路径是" + path_in_dict)


# set_dictvalue(test_dict, "list[0].sublist[0].sub1", 123345446)
# print(test_dict)


def get_path(source_dict, path_in_dict):
    exp = parse(path_in_dict)
    matched_items = exp.find(source_dict)
    return matched_items[0].value


# print(get_path(test_dict, "list[0].sublist[0]"))
#
# for item in test_dict.get("none", {}):
#     print("nothing")
#
# print("$TEST"[1:])
#
# expected = {"expected": {
#     "result[0].category.id": "{{categoryId}}",
#     "result[0].foods[0].id": "{{foodId}}"
# }}
#
# print(str(expected.get("expected")))
# test_dict = {"categoryId": 123, "foodId": 1234}
# result = Template(str(expected.get("expected"))).render(test_dict)
# print(eval(result))
# print(type(eval(result)))
#
new_expected = {
    "pre_action": {"expected.result[0].category.id": "categoryId", "expected.result[0].foods[0].id": "foodId"},
    "params": {'restaurantId': ''},
    "expected": {
        "result[0].category.id": '',
        "result[0].foods[0].id": ''
    }
}

set_dictvalue(new_expected,"expected.result[0].category.id","categoryId")
print(new_expected)
