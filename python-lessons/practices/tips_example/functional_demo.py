# -*- coding:utf-8 -*-
from functools import reduce

result = map(str,range(10))
print(type(result))
print(result)

def filter_al(x):
    return x.isalnum()

seq=["foo","x41","?!","***"]
filter(filter_al,seq)
print(seq)

seq=["foo","x41","?!","***"]

filter(lambda x:x.isalnum,seq)
print(seq)

numbers = [1,2,34,5465,57567]
result= reduce(lambda x,y:x+y,numbers)
print(result)