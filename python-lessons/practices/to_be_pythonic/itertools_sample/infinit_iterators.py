# -*- coding: utf-8 -*-
from itertools import count, cycle, repeat



for item in repeat(10,2):
    print(item)

for item in cycle('abcd'):
    print(item)

for item in count(10):
    print(item)


