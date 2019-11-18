# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     singleton_demo
   Description :
   Author :        patrick
   date：          2019/11/18
-------------------------------------------------
   Change Activity:
                   2019/11/18:
-------------------------------------------------
"""
from functools import wraps

__author__ = 'patrick'


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        print("new methods")
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MySingleton(Singleton):
    a = 1


one = MySingleton()
two = MySingleton()

print(id(one))
print(id(two))


def as_singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        print("setup")
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]


@as_singleton
class DemoClass(object):
    b = 1


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass():
    __metaclass__ = SingletonMeta


print(id(MyClass()))
print(id(MyClass()))
