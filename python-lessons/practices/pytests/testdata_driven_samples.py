#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import pytest

test_data = {
    (datetime(2011, 12, 12), datetime(2011, 12, 11), timedelta(1)),
    (datetime(2014, 12, 12), datetime(2014, 12, 13), timedelta(-1)),
}


@pytest.mark.parametrize("a,b,expected", test_data)
def test_time_distance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


def idfn(val):
    if isinstance(val, (datetime,)):
        return val.strftime('%Y%m%d')


@pytest.mark.parametrize("a,b,expected", test_data, ids=['forward', 'backward'])
def test_time_distance_v2(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a,b,expected", test_data, ids=idfn)
def test_time_distance_v3(a, b, expected):
    diff = a - b
    assert diff == expected

def test_simple():
    assert 0 == 0


