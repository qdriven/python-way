# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     context_demo
   Description :
   Author :        patrick
   date：          2019/11/18
-------------------------------------------------
   Change Activity:
                   2019/11/18:
-------------------------------------------------
"""
from contextlib import contextmanager
from math import sqrt

__author__ = 'patrick'


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __enter__(self):
        print("entry.......")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_tb, exc_val)

    def get_distance(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))


with Point(3, 4) as pt:
    print(pt.get_distance())

with Point(3, 12) as pt:
    print(pt.get_distance())


def yield_fun(x, y):
    return x * x + y * y


@contextmanager
def point(x, y):
    print('before yield')
    yield yield_fun(x, y)
    print('after yield')


with point(3, 4) as value:
    print('value is: %s' % value)
