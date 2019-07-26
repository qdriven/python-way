#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_parameters(**kwargs):
    for item in kwargs:
        print(item)


def print_parameters(**kwargs):
    for item in kwargs:
        print(item)
        print(kwargs[item])


def parameters_to_dict(**kwargs):
    result = dict()
    for k, v in kwargs.items():
        result[k] = v
    print(result)


def parameters_to_dict_oneline(**kwargs):
    result = dict((k, v) for k, v in kwargs.items())
    print(result)
    print("another methods: ")
    print(kwargs.get("params",{}))


read_parameters()
read_parameters(key='key1', value='value1')
print_parameters(key='key1', value='value1')
parameters_to_dict(key='key1', value='value1')
parameters_to_dict_oneline(key='key1', value='value1')
