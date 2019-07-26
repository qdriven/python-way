# -*- coding: utf-8 -*-

def product(a, b):
    print("a is %d" % a)
    print("b is %d" % b)
    return a * b


argument_tuple = (1, 2)
argument_dict = {'a': 1, 'b': 2}
argument_list = [1,2]
# interesting for unpacking
print(product(*argument_list))
print(product(*argument_tuple))
print(product(**argument_dict))
