# -*- coding: utf-8 -*-

class BaseObject(object):
    __protocal__ = 'test1'

    def __init__(self):
        self.test_context = {}


class ExtendedObject1(BaseObject):
    def test_1(self):
        print(self.__protocal__)
        self.test_context['test'] = 'cdacd'


class ExtendedObject2(BaseObject):
    __protocal__ = 'Test2'

    def test_2(self):
        print(self.__protocal__)
        print(self.test_context)


ExtendedObject1().test_1()
ExtendedObject2().test_2()
print(ExtendedObject2().__protocal__)
print(ExtendedObject1().__protocal__)


## Logging Thoughts
# 1. setup in every method,get method name,
# 2. capture requests in api call
# 3.
