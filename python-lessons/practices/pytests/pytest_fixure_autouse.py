#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass

from datetime import time, datetime

import pytest


@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('user        : %s' % getpass.getuser())
    print('module      : %s' % request.module.__name__)
    print('-----------------')


@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % datetime.now())
    print('-----------------')


def test_one():
    print('in test_one()')


def test_two():
    print('in test_two()')

## test dicovery
# I just try to do this, and at seems to work nicely:
#
# Name my test modules/files starting with ‘test_’.
# Name my test functions starting with ‘test_’.
# Name my test classes starting with ‘Test’.
# Name my test methods starting with ‘test_’.
# Make sure all packages with test code have an ‘init.py’ file.