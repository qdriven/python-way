# -*- coding:utf-8 -*-
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))

print('Items:')

for k, v in m.items():
    print('{}={}'.format(k, v))

print('"d" in m : {}'.format(('d' in m)))

print("c={}".format(m['c']))
## sorting
m.maps = list(reversed(m.maps))
print(m.maps)
print("c={}".format(m['c']))

# This stacking behavior is what makes it convenient to
# use ChainMap instances as template or application contexts.
# Specifically, it is easy to add or update values in one iteration,
# then discard the changes for the next iteration.

m2 = m.new_child()
print(m)
print(m2)
m2['c']='E'

print(m)
print(m2)