# -*- coding:utf-8 -*-
import itertools

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("First Four:", a[:4])
print("Last Four:", a[-4:])
print("4-6:", a[4:6])

a[2:3] = ['oo', 'o1']
print(a)

# reference, a and b is pointing to same place
b = a
assert a is b
print(a[::2])
print(a[1::2])
a[:] = [101, 102, 103]
print(a)
print(b)

print(itertools.islice(a, 5))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x * x for x in a]
print(squares)

squares_1 = map(lambda x: x ** 2, a)
print(squares_1)
print(a)
even_squares = [x**2 for x in a if x%2==0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x: x%2==0,a))
print(alt)

