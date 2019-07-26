# -*- coding: utf-8 -*-

class SampleClass(object):
    def __int__(self):
        print(self.__module__)

    def test_locals(self):
        print(self.__module__)
        print(locals())


SampleClass().test_locals()
