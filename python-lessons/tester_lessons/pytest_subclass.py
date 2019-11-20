# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     pytest_subclass
   Description :
   Author :        patrick
   date：          2019/11/20
-------------------------------------------------
   Change Activity:
                   2019/11/20:
-------------------------------------------------
"""
import pytest

from tester_lessons.pytest_parameterize import TestParameterizeWithLambda, PytestConfig, issues

__author__ = 'patrick'

PytestConfig.factor = 12


class TestSubclass(TestParameterizeWithLambda):
    @pytest.mark.parametrize("id_num", issues(factor=PytestConfig.factor))
    def test_issue(self, id_num):
        self.issue_check(id_num)
