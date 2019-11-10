# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     class_inheritance_polymorphism
   Description :
   Author :        patrick
   date：          2019/11/10
-------------------------------------------------
   Change Activity:
                   2019/11/10:
-------------------------------------------------
"""
__author__ = 'patrick'


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s.' % self.name)


class Cat(Animal):
    def greet(self):
        print('MiaoMiao.., I am %s' % self.name)


def hello(animal):
    animal.greet()

dog=Dog("dog")
cat=Cat("cat")

hello(dog)
hello(cat)
