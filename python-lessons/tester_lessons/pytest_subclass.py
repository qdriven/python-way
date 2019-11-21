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

from tester_lessons.case_loader import load_cases_from_excel, load_case_by_yml
from tester_lessons.pytest_parameterize import TestParameterizeWithLambda, PytestConfig, issues

__author__ = 'patrick'

PytestConfig.factor = 12


@pytest.mark.parametrize("id_num", (1, 2, 3, 4, 5))
def test_issue_plain(id_num):
    print(id_num)


#
# class TestSubclass(TestParameterizeWithLambda):
#     @pytest.mark.parametrize("id_num", issues(factor=PytestConfig.factor))
#     def test_issue(self, id_num):
#         self.issue_check(id_num)

@pytest.mark.parametrize("test_desc,input,expected", load_case_by_yml("testcases.yml"))
def test_issue_plain(test_desc, input, expected):
    print(test_desc, input, expected)
