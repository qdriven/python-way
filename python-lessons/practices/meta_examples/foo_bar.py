# -*- coding:utf-8 -*-


class FooBar(object):
    def __init__(self):
        self.var1 = "var1"

print(FooBar.__mro__)

# DYNAMISM we can not be sure of what members
# an instance will have at any given time

myobj = FooBar()
try:
    myobj.my_custom_var = 123
    print(myobj.my_custom_var)
    # get attributes
    print(hasattr(myobj, "var1"))
    setattr(myobj, "var1", "234")
    print(getattr(myobj, "var1"))
except Exception as e:
    print(e)
print(myobj)

print(int.__class__)


class NewInitSample(object):
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        for arg in args:
            print(arg)
        for kwarg in kwargs:
            print(kwarg)
        return super(NewInitSample, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print("in __init__")
        self.bar = 123


new_init_instance = NewInitSample()
print(new_init_instance.bar)


## metaclass are the way to customize their creation
## the base metaclass is type, tyep's type is type


## What does a metaclass do

class MyType(type):
    def __new__(cls, *args, **kwargs):

        print("in __new__")
        for arg in args:
            print(arg)
        for kwarg in kwargs:
            print(kwarg)
        return super(MyType, cls).__new__(cls, *args, **kwargs)

        # def __new__(cls, name, parents, dct):
        #     # this method has the responsability to
        #     # create and return a new instance of type
        #     # the only way to do so is to call type itself (or any subclass)
        #     print("A new class named " + name + " is going to be created")
        #     return super(MyType, cls).__new__(cls, name, parents, dct)


class MyObject(object):
    __metaclass__ = MyType


# meta class lookup:
#     1. on the class
#     2. parents
#     3. package

my_obj = MyObject()
print(my_obj)
