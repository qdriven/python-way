#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='function', params=None, autouse=False)
def before(request):
    print("\n fixture before")


# Return value
# Finalizer is teardown
# Request objects
# Scope
# Params
# Toy example
# Real example
# Autouse
# Multiple fixtures
# Modularity: fixtures using other fixtures

# return value
@pytest.fixture(scope='module')
def some_data(request):
    data = {'foo': 1, 'bar': 2}

    def fin():
        print("adding to finalizer")

    print('\n-----------------')
    print('fixturename : %s' % request.fixturename)
    print('scope       : %s' % request.scope)
    # print('function    : %s' % request.function.__name__)
    # print('cls         : %s' % request.cls)
    print('module      : %s' % request.module.__name__)
    print('fspath      : %s' % request.fspath)
    print('-----------------')
    request.params = {"key1":"values"}
    request.addfinalizer(fin)  ## tear down
    return data


def test_foo(some_data,request):
    print(some_data)
    print('\n-----------------')
    print('fixturename : %s' % request.fixturename)
    print('scope       : %s' % request.scope)
    print('function    : %s' % request.function.__name__)
    print('cls         : %s' % request.cls)
    print('module      : %s' % request.module.__name__)
    print('fspath      : %s' % request.fspath)
    print('params : %s' % request.params)
    print('-----------------')
    assert some_data['foo'] == 1

def test_bar(some_data):
        print(some_data)
        assert some_data['bar'] == 2

# function	Run once per test, it is default
# class	Run once per class of tests
# module	Run once per module
# session	Run once per session