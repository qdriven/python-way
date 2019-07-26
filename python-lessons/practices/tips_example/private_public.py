# -*- coding:utf-8 -*-

class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self._private_field = 10

    def get_private_field(self):
        return self._private_field

    @classmethod
    def get_private_field_for(cls, instance):
        return instance._private_field


bar = MyObject()
print(MyObject.get_private_field_for(bar))
print(bar.get_private_field_for(bar))


class MyObjectChild(MyObject):
    def __init__(self):
        pass

    def get_private_field(self):
        return self._private_field


child = MyObjectChild()
print(child.get_private_field())
print(dict(child))


## getattr,getattribute,setattr