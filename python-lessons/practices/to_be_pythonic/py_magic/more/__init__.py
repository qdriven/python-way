# -*- coding: utf-8 -*-

def more_function():
    print("this is more")


def common_func(*args,**kwargs):
    for a in args:
        print("list")
        print(a)
    for item in kwargs:
        print("key, value pair")
        print(item)