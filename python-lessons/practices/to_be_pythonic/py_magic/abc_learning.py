# -*- coding: utf-8 -*-

# descriptor objects
class Meter(object):
    '''Descriptor for a meter.'''

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        print(type(instance))
        self.value = float(value)


class Foot(object):
    '''Descriptor for a foot.'''

    def __get__(self, instance, owner):
        print(owner)
        print(type(instance))
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    '''Class to represent distance holding two descriptors for feet and
    meters.'''
    meter = Meter(1.0)
    foot = Foot()


class NewDistance:
    def __init__(self, value=0):
        self.meter = Meter(value=value)
        self.foot = Foot()


d = Distance()
print(d.meter)
print(d.foot)
d.foot = 6.5616
print(d.meter)

nd = NewDistance(12)
print(nd.meter)
print(nd.foot)

# __copy__ __deepcopy__

# pickling your objects

import pickle

data = {'foo': [1, 2, 3],
        'bar': ('Hello', 'world!'),
        'baz': True}

with open('data.txt', 'wb') as jar:
    pickle.dump(data, jar)

with open('data.txt', 'rb') as jar:
    data = pickle.load(jar)
    print(data)

with open('string.txt','w') as f:
    f.write("this is test")


# pickle protocol
# __getinitargs__,
