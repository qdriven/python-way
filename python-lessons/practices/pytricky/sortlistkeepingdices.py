# -*- coding: utf-8 -*-


"""Sort a list and store previous indices of values"""

# enumerate is a great but little-known tool for writing nice code

l = [4, 2, 3, 5, 1]
print("original list: ", l)

values, indices = zip(*sorted((a, b) for (b, a) in enumerate(l)))

# now values contains the sorted list and indices contains
# the indices of the corresponding value in the original list

print("sorted list: ", values)
print("original indices: ", indices)

# note that this returns tuples, but if necessary they can
# be converted to lists using list()

print(list((a, b) for b, a in enumerate(l)))
# print(zip(list((a,b) for b,a in enumerate(l))))
print(sorted((a, b) for b, a in enumerate(l)))

values, indices = zip(*sorted((a, b) for (b, a) in enumerate(l)))
print(values)
print(indices)
