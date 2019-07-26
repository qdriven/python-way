# -*- coding:utf-8 -*-
import bisect
# Bisection algorithms.
# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

# insort, insert a data into a sorted list while maintaining the list in sorted
l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3}  {:3}'.format(i, position), l)

# insort_left or insort_right=insort

l = []
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3}  {:3}'.format(i, position), l)