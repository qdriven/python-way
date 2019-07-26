# -*- coding:utf-8 -*-

class Person:
    def __init__(self):
        self.name="name"
        self.age=12
p= Person()
print(hasattr(p,"name"))

setattr(p,"test","value")
print(p.test)



