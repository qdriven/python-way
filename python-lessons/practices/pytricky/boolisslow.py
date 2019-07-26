# -*- coding: utf-8 -*-

"""
True and False are keywords in python3, but not in Python2. In Python2
the value of True is 1, and the value of False is 0.
True and False can be
regarded as vars and thus they are slow in while loop.

By the way, True and False can be changed in Python2.

Note: This leads to a performance improvement only in Python2.
"""
from timeit import timeit


def test_true():
    count = 100
    while True:  # Here is True
        if count < 0:
            break
        count = -1


def test_1():
    count = 100
    while 1:
        break
    count -= 1


print('use True: %s' %timeit(test_true, number=1000000))
print('use 1: %s' % timeit(test_1, number=1000000))
