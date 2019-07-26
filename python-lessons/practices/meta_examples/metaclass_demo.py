# type: the base metaclass
# __new__/__init__
# metaclass custom the object creation way
from abc import ABCMeta


class MyMeta(type):
    """
    custom creating type
    """

    def __new__(cls, name, parents, dct):
        print("A new class named " + name + " is going to be created")
        return super(MyMeta, cls).__new__(cls, name, parents, dct)


class MyClass(object):
    __metaclass__ = MyMeta


# lookup order:
# - on the class
# - in the parents
# - in the package

mc = MyClass()
print(mc)


class MyABCMeta:
    __metaclass__ = ABCMeta
