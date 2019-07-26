# -*- coding: utf-8 -*-
"""
    A function that references variables from a containing scope,
    potentially after flow-of-control has left that scope
    A function that can refer to environments that are no longer active.
    A closure allows you to bind variables into a function without passing them as parameters.
"""
def make_counter():
    i =0
    def counter():
        nonlocal i
        i+=1
        return i
    return counter

c1=make_counter()
c2=make_counter()
print(c1(),c1(),c2(),c2())
print(c1(),c1(),c2(),c2())
