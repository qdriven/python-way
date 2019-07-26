# -*- coding: utf-8 -*-

class CustomOperator:
    def __init__(self, id):
        self.id = id
        pass

    def __cmp__(self, other):
        print("comparing")
        return self.id > other.id

    def __eq__(self, other):
        print("eq")
        return self.id == other.id

    def __gt__(self, other):
        print("greater than")
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def __ge__(self, other):  # >=
        pass

    def __le__(self, other):  # <=
        pass

    def __str__(self):
        return self.id

    def __repr__(self):
        return "operator id:%s"%str(self.id)

o1=CustomOperator(12)
o2=CustomOperator(14)

print(o1 > o2)

print(sorted([o1,o2]))

# numeric magic methods
# normal arithmetic operators
# reflected arithmetic operators
# augmented assignment
# type conversion
# __int__() __long__ __float__ __complex__ __hex__
# representing your classes: __str__,__repr__,__unicode__ __format__ __hash__ __nonzero__ __dir__

class TypeClass:
    def __init__(self,num):
        self.num=num

    def __int__(self):
        return len(self.num)

    def __dir__(self):
        print("this is Type CLass")
        return locals()


print(int(TypeClass("pathic")))
m = TypeClass("pathic")

print(dir(m))