#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func1(name):
    print(name)


def func2(name):
    print(name)


print(callable(func1))

for item in ['func1', 'func2']:
    locals()[item]('test')


class Test1:
    def __init__(self):
        pass

    def test_1(self):
        print("test1")

    def test_2(self):
        print("test2")

    def test_3(self):
        print("test3")

    def print_local_methods(self):
        for element in ['test_1', 'test_2', 'test_3']:
            method=getattr(self,element)
            method()

Test1().print_local_methods()