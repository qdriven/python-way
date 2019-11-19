# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     case_loader
   Description :
   Author :        patrick
   date：          2019/11/18
-------------------------------------------------
   Change Activity:
                   2019/11/18:
-------------------------------------------------
"""
import ast
import json

import yaml

__author__ = 'patrick'

## Load Test Case from Excel
## Load Test Case from YML


from openpyxl import load_workbook


def load_cases_from_excel(path="./api_testcases.xlsx"):
    wb = load_workbook(path)
    ws = wb.active
    count = 0
    headers = []
    result = []
    for row in ws.rows:
        if count == 0:
            print(row)
            for item in row:
                headers.append(item.value)
        count += 1

        col_count = 0
        tup = tuple()
        for column in row:
            tup += (yaml.safe_load(column.value),)
        result.append(tup)
    return result


def load_case_by_yml(path):
    with open(path, 'r') as stream:
        raw_yaml_result = yaml.safe_load(stream)
    cases = raw_yaml_result["tests"]
    ## todo: add cases
    parameterized_case = []
    for case in cases:
        parameterized_case.append(tuple(case.values()))
    return parameterized_case


result = load_cases_from_excel()
print(result)
cases = load_case_by_yml("./testcases.yml")
print(cases)
