# -*- coding: utf-8 -*-
import pytest
from pytests.pytest_xunit import BaseTest

test_data = [
    {'foo': {"shopId": 1}, 'bar': 2},
    {'foo': {"shopId": 2}, 'bar': 3},
]


@pytest.fixture(params=test_data)
def fixture_test_data(request):
    return request.param

class TestBase(BaseTest):

    def test_name(self):
        print(__name__)
    def test_abded(self,fixture_test_data):
        print(fixture_test_data)
        print("dsafdsagd")

    def mixture(self):
        print("mixture")

    def test_abcd(self):
        print("test abcds")
        assert 1 == 1
