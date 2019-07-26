# -*- coding: utf-8 -*-


"""nested functions"""
def addBy(val):
    print(val)
    def func(inc):
        print(inc)
        return val + inc
    return func

addFive = addBy(5)
print(addFive(4))

addThree = addBy(3)
print(addThree(7))
