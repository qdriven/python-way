# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     slot_demo
   Description :
   Author :        patrick
   date：          2019/11/18
-------------------------------------------------
   Change Activity:
                   2019/11/18:
-------------------------------------------------
"""
__author__ = 'patrick'


class SlotDemo:
    __slots__ = ('x', 'y', 'z', 'w')

    def __init__(self, x=0, y=0):
        self.x = 10
        self.y = y


class SlotSubClass(SlotDemo):

    def __init__(self):
        super(SlotSubClass, self).__init__()
        print(dir(self))


slot = SlotDemo(1, 2)
print(slot.x, slot.y)
slot.z = 10
slot.w = 10

print(dir(slot))

sub = SlotSubClass()
print(sub.x)
sub.x = 100
sub.y = 100
dir(sub)
