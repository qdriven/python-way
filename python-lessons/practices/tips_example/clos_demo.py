# -*- coding:utf-8 -*-
def sort_priority(source, given_group):
    found = False

    def helper(x):
        for x in given_group:
            found = True
            return 0, x
        return 1, x

    source.sort(key=helper)
    return found


values = [1, 5, 3, 9, 7, 4, 2, 8, 6]
group = [7, 9]

sort_priority(values, group)
print(values)


class Sorter(object):
    def __init__(self, given_group):
        self.group = given_group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x

# nonlocal usage
sorter = Sorter(group)
values.sort(key=sorter)
print(sorter.found)
