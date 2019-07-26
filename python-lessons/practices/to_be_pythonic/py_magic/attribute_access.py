# -*- coding: utf-8 -*-


class AttributeAccess:
    def __int__(self):
        print("init attribute access")

    def __getattr__(self, item):
        print("name is ", item)
        return "missing " + item

    def __setattr__(self, key, value):
        super(AttributeAccess,self).__setattr__(key,value)

    def __delattr__(self, item):
        pass

    def __getattribute__(self, item):
        """
        not recommend to use it, only be used in new-style class
        :param item:
        :return:
        """
        pass

    def __repr__(self):
        return self

    def __str__(self):
        return  str(self.__dict__)

a = AttributeAccess()
a.test = 12

print(a.test)
print(a.ntest)


class AccessCounter(object):
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''

    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # Make this unconditional.
        # If you want to prevent other attributes to be set, raise AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)