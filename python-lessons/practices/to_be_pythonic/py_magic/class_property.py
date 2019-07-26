# -*- coding: utf-8 -*-
from to_be_pythonic.py_magic import status


class BaseClass(object):
    test_context = dict()
    flag = True

    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def run(self):
        if status.base_name:
            status.base_name = False
            print("base name is true")
        else:
            print("base name is false")
        self.test_context["test"] = status.base_name


class BaseClassE(BaseClass):
    def __init__(self):
        pass

    def run(self):
        self.flag = False
        self.test_context["base class E"] = "abcds"


bc = BaseClass()
bc.name = "test"
print(bc.name)
print(bc.run())

bc1 = BaseClassE()
print(bc1.run())
print(bc1.test_context)
print(bc.flag)
print(bc1.flag)
