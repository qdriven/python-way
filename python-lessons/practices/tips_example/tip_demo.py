# -*- coding:utf-8 -*-


def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError as e:
        return ValueError("Invalid inputs,error=" + e)


x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print("Invalid Inputs")
else:
    print("Result is %.1f" % result[1])


