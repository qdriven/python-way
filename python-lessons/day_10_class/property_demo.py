# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     property_demo
   Description :
   Author :        patrick
   date：          2019/11/13
-------------------------------------------------
   Change Activity:
                   2019/11/13:
-------------------------------------------------
"""
__author__ = 'patrick'


class PropertyDemo:

    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val


p = PropertyDemo(12)
print(p.score)
