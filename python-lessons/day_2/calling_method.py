# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     calling_method
   Description :
   Author :        patrick
   date：          2019/9/22
-------------------------------------------------
   Change Activity:
                   2019/9/22:
-------------------------------------------------
"""
__author__ = 'patrick'


def method_1():
    print("this is method1")


def method_2(arg1):
    print("this is " + arg1)


def method_3(*args):
    for arg in args:
        print(arg)


def method_4(arg1, arg2):
    print(arg1, arg2)


def method_5(arg1, arg2, *args):
    method_4(arg1, arg2)
    method_3(args)


def method_6(*args, **kwargs):
    method_3(args)
    for k, v in kwargs.items():
        print(k, v)
