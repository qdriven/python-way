# -*- coding: utf-8 -*-

"""
True and False can be used as integer values
"""

a = 5

print(isinstance(a,int)+(a<10))
# interesting writing
print(["is odd","is even"][a % 2 ==0])
print("is even" if a % 2 ==0 else "is odd")