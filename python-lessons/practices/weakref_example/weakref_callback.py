# -*- coding:utf-8 -*-
import weakref

import gc


class ExpensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
    print('callback({!r})'.format(reference))


def on_finalize(*args):
    print('on_finalize({})'.format(args))


obj = ExpensiveObject()
obj_id = id(obj)
r = weakref.ref(obj, callback)
f = weakref.finalize(obj, on_finalize, 'extra arguments')
f.atexit = False
print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())
for o in gc.get_objects():
    if id(o) == obj_id:
        print('Found uncollected object in gc')
