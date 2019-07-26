# -*- coding:utf-8 -*-

class MagicClass:
    def __init__(self):
        self.value = "mc"
        print("this is __init__")

    def __del__(self):
        print("this is del")


class MC1(MagicClass):
    def __init__(self):
        pass


class MC2(MagicClass):
    def __init__(self):
        super(MC2, self).__init__()


mc = MagicClass()
print(mc.value)
del (mc)
mc1 = MC1()
try:
    print(mc1.value)
except Exception as e:
    print(e)
mc2 = MC2()
print(mc2.value)


# __getitem__,__setitem__,__delitem__

class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        print("get item from __getitem__")
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

    def __setitem__(self, index, value):
        print("set items")
        self.counter += 1
        return super(CounterList, self).__setitem__(index, value)


cl = CounterList(range(100))
cl.reverse()
print(cl)
print(cl[9])
cl[10] = 6
print(cl)


# property

class Shape:
    def __init__(self):
        self.round = 10

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        return self.__dict__.get(key, "")

    def __str__(self):
        return str(self.__dict__)


shape = Shape()
shape.name = "test"
shape.params = "params"

print(shape)


class TestIterator:
    value = 0

    def __next__(self):
        print("next is invoked")
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
print(list(ti))


class Fibs:
    def __init__(self, top):
        self.a = 0
        self.b = 1
        self.counter = top

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.counter -= 1
        return self.a

    def __iter__(self):
        return self


fibs = Fibs(10)
for fib in fibs:
    print(fib)

