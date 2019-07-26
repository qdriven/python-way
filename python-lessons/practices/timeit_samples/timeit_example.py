# -*- coding:utf-8 -*-

"""
timeit, calculate the time which the given method spends
"""
import textwrap

import timeit

"""
timeit: run setup only once, and run other method for the given times
repeat: run setup only once, and run other method for the given times in one iteration
"""
t = timeit.Timer(stmt="print('print method')", setup="print('setup')")
print("TimeIt:")
print(t.timeit(number=2))

print("REPEAT:")
print(t.repeat(3, 2))  # 3 times,every time run print method two times,setup once

# complex one
range_size = 1000
count = 1000
setup_statement = ';'.join([
    "l = [(str(x), x) for x in range(1000)]",
    "d = {}",
])


def show_results(result):
    "Print microseconds per pass and per item."
    global count, range_size
    print("timeit result:{}".format(result))
    per_pass = 1000000 * (result / count)
    print('{:6.2f} usec/pass'.format(per_pass), end=' ')
    per_item = per_pass / range_size
    print('{:6.2f} usec/item'.format(per_item))


print("{} items".format(range_size))
print("{} iterations".format(count))
print()

print('__setitem__:', end=' ')
t = timeit.Timer(
    textwrap.dedent(
        """
        for s, i in l:
            d[s] = i
        """),
    setup_statement,
)
show_results(t.timeit(number=count))

print("evaluate setdefault:", end='.......')

t = timeit.Timer(textwrap.dedent(
    """
    for s,i in l:
        d.setdefault(s,i)
    """
), setup_statement)

show_results(t.timeit(number=count))

# Using exceptions
print('KeyError   :', end=' ')
t = timeit.Timer(
    textwrap.dedent(
        """
        for s, i in l:
            try:
                existing = d[s]
            except KeyError:
                d[s] = i
        """),
    setup_statement,
)
show_results(t.timeit(number=count))

# Using "in"
print('"not in"   :', end=' ')
t = timeit.Timer(
    textwrap.dedent(
        """
        for s, i in l:
            if s not in d:
                d[s] = i
        """),
    setup_statement,
)
show_results(t.timeit(number=count))
