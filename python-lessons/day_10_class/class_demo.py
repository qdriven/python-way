# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     class_demo
   Description :
   Author :        patrick
   date：          2019/11/10
-------------------------------------------------
   Change Activity:
                   2019/11/10:
-------------------------------------------------
"""
__author__ = 'patrick'


class Animal:
    """
    first class
    """
    pass


first_instance = Animal()
print(id(first_instance))
second_animal = Animal()
# different address/different instance
print(id(second_animal))


class NamedAnimal(Animal):
    def __init__(self, name: str):
        """
        python magic method，特殊方法
        :param name:
        """
        self.__name = name

    def name(self) -> str:
        return self.__name


named_animal = NamedAnimal("name")
print(named_animal.name())
print(type(named_animal))
print(type(123))
print(type("b"))
try:
    # 在
    # Python
    # 中，以双下划线开头，并且以双下划线结尾（即
    # `__xxx__`）的变量是特殊变量，特殊变量是可以直接访问的
    named_animal.__name  ## private ,can't access
except Exception as e:
    print(e)

print(isinstance("ncd",str))

print(hasattr(named_animal,"name"))
print(hasattr(named_animal,"__name")) # why false?
print(hasattr(named_animal,"__init__"))
print(hasattr(named_animal,"__init__"))
print(hasattr(named_animal,"__init"))
print(hasattr(named_animal,"hashcode"))
print(dir(named_animal))

print(getattr(named_animal,"name"))
print(type(getattr(named_animal,"name")))


