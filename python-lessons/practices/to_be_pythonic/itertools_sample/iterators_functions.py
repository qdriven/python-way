# -*- coding: utf-8 -*-
import operator
from itertools import accumulate, repeat

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(accumulate(data, operator.mul)))

data = [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
print(list(accumulate(data, max)))

# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
print(list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))

# Chaotic recurrence relation https://en.wikipedia.org/wiki/Logistic_map
r=3.8
logistic_map = lambda x, _:  r * x * (1 - x)
input = repeat(0.4,36)
print([format(x, '.2f') for x in accumulate(input, logistic_map)])
