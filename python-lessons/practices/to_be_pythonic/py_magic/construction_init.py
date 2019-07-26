# -*- coding: utf-8 -*-

"""
__new__(cls,[....): a first method to get called in an object's instantiation
__init__(self,[....): the initializer for the class. It gets passed the whatever primary constructor was called
__del__(self) : __del__, destructor
"""


class Foo:

    def __init__(self,name):
        self.name=name
        print('init Foo with name:%s'%self.name)

    def __del__(self):
        """
        behavior for gc
        :return:
        """
        print("destruct Foo name %s"%self.name)

print(Foo('foo'))