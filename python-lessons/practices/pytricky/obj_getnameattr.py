# -*- coding: utf-8 -*-
""" Return the value of the named attribute of an object """


class obj():
    attr = 1

    def __getattribute__(self, item):
        print('get attribute')
        return "123"

    def __get__(self, instance, owner):
        print("get")

    def __getattr__(self, item):
        print("get attribute1")


foo = "attr"
a = obj()
print(a.test)
print(getattr(obj, foo))
print(getattr(a, "attr1"))
