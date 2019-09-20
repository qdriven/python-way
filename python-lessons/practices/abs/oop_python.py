# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     oop_python
   Description :
   Author :        patrick
   date：          2019/7/30
-------------------------------------------------
   Change Activity:
                   2019/7/30:
-------------------------------------------------
"""
__author__ = 'patrick'


class Pizza:

    def __init__(self, size=10):
        self.size = size

    def get_size(self):
        return self.size


try:
    print(Pizza.get_size)
except Exception as e:
    print(e)

print(Pizza.get_size(Pizza(42)))
m =Pizza(43).get_size
print(m())
print(Pizza().get_size())
