#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Animal:
    __its_name__ = "animal"

    def __init__(self):
        pass

    def print_name(self):
        print(self.__its_name__)


class Cat(Animal):
    __its_name__ = "Cat"


Cat().print_name()
Animal().print_name()