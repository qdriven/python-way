# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     iter_demo
   Description :
   Author :        patrick
   date：          2019/11/24
-------------------------------------------------
   Change Activity:
                   2019/11/24:
-------------------------------------------------
"""
import collections
from typing import Iterator

__author__ = 'patrick'

it = iter([1, 2, 3, 4])
print(it)
while (True):
    try:
        print(next(it))
    except StopIteration as e:
        print(e)
        break


class Fib:
    def __init__(self):
        self._prev = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._prev, self._next = self._next, self._prev + self._next
        return self._prev


if __name__ == '__main__':
    fib = Fib()
    print(isinstance(fib, Iterator))
    print(isinstance(fib, collections.abc.Iterator))
    for f in fib:
        print(f)
        if f > 100:
            break

"""
- [Callback or Iterator in Python](https://code-maven.com/callback-or-iterator-in-python)
"""
