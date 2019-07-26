# -*- coding: utf-8 -*-

class Entity:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __call__(self):

        return self.x+self.y

e=Entity(1,2)
print(callable(e))

print(e())