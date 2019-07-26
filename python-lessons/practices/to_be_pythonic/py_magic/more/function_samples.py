# -*- coding: utf-8 -*-
import time
import more


def foo():
    print("bar")


print(foo.__name__)
print(time.time.__name__)

more_func = getattr(more, 'more_function')
more_func()

more.common_func("a", "b", bar="bar", test="test")


class ExampleClass:
    def __init__(self, **kwargs):
        self.val = kwargs.get('val', "val")
        self.val2 = kwargs.get('val2', "val2")


print(ExampleClass(val2="test", val="testing").val)


# iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):  # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter(3, 8):
    print(c)


def counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1


for item in counter(3, 9):
    print(item)


def print_everything(**kwargs):
    for count, thing in enumerate(kwargs):
        print('{0}.{1}'.format(count, thing))


print_everything(test="test", test1="test1")
my_list = ["list", "test", "missing"]


def print_missing(*args):
    for item in args:
        print(item)


print_missing(*my_list)
