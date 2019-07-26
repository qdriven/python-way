# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     check_duplication
   Description :
   Author :        patrick
   date：          2019/7/9
-------------------------------------------------
   Change Activity:
                   2019/7/9:
-------------------------------------------------
"""
__author__ = 'patrick'

"""
In Order to remove the duplication item in a list
The question is:
1. Data Structure Difference Between List And Set
2. Why Set can Remove Duplicated Element
"""

lst = ['a', 'b', 'a']
print(len(lst))
removed_dup = set(lst)
print(len(removed_dup))
print(removed_dup)
print(removed_dup.pop())
print(len(removed_dup))

