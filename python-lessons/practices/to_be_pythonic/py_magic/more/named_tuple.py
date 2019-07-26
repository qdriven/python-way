# -*- coding: utf-8 -*-
from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', 'x,y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.0, 4.0)

x1, y1 = pt1  # unpacking

print(x1, y1)


def line_length(pt1, pt2):
    return (sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2))


def line_length_index(pt1, pt2):
    return (sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2))


print(line_length(pt1, pt2))
print(line_length_index(pt1, pt2))
# immutable for set
pt1.x = 10

# mutable record type [record type](http://code.activestate.com/recipes/576555/)
