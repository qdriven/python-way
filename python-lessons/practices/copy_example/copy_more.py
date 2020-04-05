# -*- coding:utf-8 -*-
import functools

import copy


@functools.total_ordering
class MyClass:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return len(self.name) > len(other.name)

    def __copy__(self):
        print("__copy__")
        return MyClass(self.name)

    # The memo dictionary is used to keep track of the values
    # that have been copied already, so as to avoid infinite recursion.
    def __deepcopy__(self, memodict={}):
        print("__deepcopy__{}".format(memodict))
        return MyClass(copy.deepcopy(self.name, memodict))


if __name__ == '__main__':
    a = MyClass("a")
    sc = copy.copy(a)
    dc = copy.deepcopy(a)
    print("a is {}".format(a))

    print("copy object is {}".format(sc))
    print("a.name is copy object.name ? {}".format(a.name is sc.name))
    print("deepcopy object is {}".format(dc))
    print("a.name is deepcopy object.name ? {}".format(a.name is dc.name))
