# -*- coding:utf-8 -*-
from collections import defaultdict


def log_missing():
    print("Key added")
    return 0


current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]
# hook for defaultdict
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, increment in increments:
    result[key] += increment
print("After:", dict(result))

# todo: __call__ usage
def increment_with_report(current, increments):
    add_count = 0

    def missing():
        nonlocal add_count
        add_count += 1
        return 0

    value_result = defaultdict(missing, current)
    for key, value in increments:
        value_result[key] += value
    return value_result, add_count
