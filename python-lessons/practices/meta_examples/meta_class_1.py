# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     meta_class_1
   Description :
   Author :        patrick
   date：          2019/2/1
-------------------------------------------------
   Change Activity:
                   2019/2/1:
-------------------------------------------------
"""
__author__ = 'patrick'


# generator
# decorator
# context manager

class Base1:
    def foo(self):
        print("foo")


class DerivedBase(Base1):
    def bar(self):
        print("bar")
