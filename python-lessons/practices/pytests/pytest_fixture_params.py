#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

test_data = [
    {'foo': {"shopId": 1}, 'bar': 2},
    {'foo': {"shopId": 2}, 'bar': 3},
]


@pytest.fixture(params=test_data)
def fixture_test_data(request):
    return request.param


def setup_module(module):
    print(module)
    print(module)


def teardown_module(module):
    print(module)
    print(module)


def setup_method(method):
    print(method)
    print(method)


def test_note_1(fixture_test_data, request):
    print(fixture_test_data)
    print(request)
    assert fixture_test_data['foo']['shopId'] > 0
