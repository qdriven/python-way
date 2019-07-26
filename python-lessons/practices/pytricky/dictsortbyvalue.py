# -*- coding: utf-8 -*-
""" Sort a dictionary by its values with the built-in sorted() function and a 'key' argument. """

d = {'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1}
print(sorted(d.items(), key=lambda x: x[1]))


""" Sort using operator.itemgetter as the sort key instead of a lambda"""


from operator import itemgetter

## todo operator usage
for item in d.items():
    print(itemgetter(0))
    print(itemgetter(1))

print(sorted(d.items(), key=itemgetter(1)))


"""Sort dict keys by value"""


print(sorted(d, key=d.get))
