#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Sample:
    def __init__(self, name):
        print(name)


class Sample1(Sample):
    def __init__(self, name):
        super(Sample1, self).__init__(name=name)


class_list = [
    (Sample, {"name": "test1"}),
    (Sample1, {"name": "test2"})
]


def run_class_dict():
    for item in class_list:
        item[0](item[1].get("name"))

run_class_dict()
