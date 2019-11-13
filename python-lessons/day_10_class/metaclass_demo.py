# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     metaclass_demo
   Description :
   Author :        patrick
   date：          2019/11/13
-------------------------------------------------
   Change Activity:
                   2019/11/13:
-------------------------------------------------
"""
__author__ = 'patrick'


class Foo:
    foo = True


print(type(10))
print(type(Foo()))
print(type(Foo))


def greeting():
    print("Hello World!")


foo = type('Foo', (), {'foo': False, 'greeting': greeting})
print(foo.foo)
foo.greeting()
print(foo)


class PrefixMetaClass(type):

    def __new__(cls, cls_name, *args, **kwargs):
        _attrs = (('my_' + name, value) for name, value in kwargs.items())
        _attrs = dict((name, value) for name, value in _attrs)
        return type.__new__(cls, cls_name, args, _attrs)


class FooMeta(metaclass=PrefixMetaClass):

   #  __metaclass__=PrefixMetaClass

    name = "foo"

    def bar(self):
        print("this is bar")


f = FooMeta()
print(f.name)
