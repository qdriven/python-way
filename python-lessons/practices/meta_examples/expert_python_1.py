# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     expert_python_1
   Description :
   Author :        patrick
   date：          2019/2/1
-------------------------------------------------
   Change Activity:
                   2019/2/1:
-------------------------------------------------
"""
__author__ = 'patrick'

# Top-level function or top-level syntax -> corresponding __
## init:__init__
## repr(x): __repr__
## size: __len__
## protocol/meta class
# x() -> __call__
# protocol vie of python
# OO Pattern


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial(*{!r}".format(self.coeffs)

    def __call__(self, *args, **kwargs):
        pass




