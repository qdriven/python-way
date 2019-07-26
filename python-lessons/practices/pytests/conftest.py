#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def pytest_addoption(parser):
    parser.addoption("--all", action="store_true", help="run all combination")


def pytest_generate_tests(metafunc):
    if 'param1' in metafunc.fixturenames:
        if metafunc.config.option.all:
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))


from _pytest.runner import runtestprotocol


# def pytest_runtest_protocol(item, nextitem):
#     reports = runtestprotocol(item, nextitem=nextitem)
#     for report in reports:
#         if report.when == 'call':
#             print('\n%s --- %s' % (item.name, report.outcome))


class CTestItem(pytest.Item):
    """
    Pytest.Item subclass to handle each test result item. There may be
    more than one test result from a test function.

    """

    def __init__(self, name, parent, test_result):
        """Overridden constructor to pass test results dict."""
        super(CTestItem, self).__init__(name, parent)
        self.test_result = test_result

    def runtest(self):
        """The test has already been run. We just evaluate the result."""
        if self.test_result["condition"] == "FAIL":
            raise CTestException(self, self.name)

    def repr_failure(self, exception):
        """
        Called when runtest() raises an exception. The method is used
        to format the output of the failed test result.

        """
        if isinstance(exception.value, CTestException):
            return ("Test failed : {TST} at {file_name}:{line_number}\n"
                    "         got: {GOT}\n"
                    "    expected: {EXP}\n".format(**self.test_result))

    def reportinfo(self):
        """"Called to display header information about the test case."""
        return self.fspath, self.test_result["line_number"] - 1, self.name


class CTestException(Exception):
    """Custom exception to distinguish C unit test failures from others."""
    pass
