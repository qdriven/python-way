# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     method_demo
   Description :
   Author :        patrick
   date：          2019/11/13
-------------------------------------------------
   Change Activity:
                   2019/11/13:
-------------------------------------------------
"""
__author__ = 'patrick'


class DemoMethods(object):
    def foo(self):
        print("Hello,", self)

    @staticmethod
    def bar():
        print("bar")

    @classmethod
    def class_bar(cls):
        print("Hello,", cls)
        print(cls.bar)


d = DemoMethods()
d.bar()
DemoMethods.bar()
DemoMethods.class_bar()
