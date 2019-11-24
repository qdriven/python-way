# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     os_demo
   Description :
   Author :        patrick
   date：          2019/11/24
-------------------------------------------------
   Change Activity:
                   2019/11/24:
-------------------------------------------------
"""
import os

__author__ = 'patrick'

print(os.path.abspath(__file__))
print(os.path.abspath('web'))
print(os.path.abspath('.'))

print(os.path.dirname("."))
print(os.path.basename(__file__))
print(os.path.splitext(__file__))
print(os.path.split(__file__))

for root, dir, file in os.walk(os.path.curdir):
    print(root, dir, file)
