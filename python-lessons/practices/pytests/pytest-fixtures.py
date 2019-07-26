#!/usr/bin/env python
# -*- coding: utf-8 -*-

# before usage
import pytest


# py.test -s <file_name>

@pytest.fixture
def before():
    print("\n before each test")


@pytest.fixture
def after():
    print("\n in each test")


def test_1(before):
    print("test_1")


def test_2(before):
    print("test2")


# three way to use a fixture

# 1. name it
# 2. usefixture
@pytest.mark.usefixtures("before")
def test_use_fixture_1():
    print('test_1()')


class TestUseFixture:
    @pytest.mark.usefixtures("before", "after")
    def test_1(self):
        print("in class test1")

    @pytest.mark.usefixtures("before")
    def test_2(self):
        print("in class test2")

