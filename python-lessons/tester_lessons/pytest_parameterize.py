# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     pytest_parameterize
   Description :
   Author :        patrick
   date：          2019/11/20
-------------------------------------------------
   Change Activity:
                   2019/11/20:
-------------------------------------------------
"""
import pytest

__author__ = 'patrick'


class PytestConfig:
    factor = 1


def issues(factor):
    print([2 * factor, 2 * factor])
    return [2 * factor, 2 * factor]


class TestParameterizeWithLambda:

    def issue_check(self, id_num):
        print(PytestConfig.factor)
        assert id_num < 6
