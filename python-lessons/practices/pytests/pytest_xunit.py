# -*- coding: utf-8 -*-

import pytest


class BaseTest(object):
    def setup_method(self, method):
        print(method)
        print(method.__name__)
        print(method.__module__)
        print(method.__module__.replace('pytests.',"").strip())
        print(pytest.cmdline)

    def setup_function(self, function):
        print(function)


