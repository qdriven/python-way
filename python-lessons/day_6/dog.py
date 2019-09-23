# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     dog
   Description :
   Author :        patrick
   date：          2019/9/22
-------------------------------------------------
   Change Activity:
                   2019/9/22:
-------------------------------------------------
"""
__author__ = 'patrick'


class Dog:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def speak(self):
        print("my name is " + self.name + "," + self.text)

    def __add__(self, other):
        return None

"""
Overloading methods
"""


