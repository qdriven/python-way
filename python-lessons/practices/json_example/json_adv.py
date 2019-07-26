# -*- coding:utf-8 -*-

# dump custom class
import json


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{{'name':'{}'}}".format(self.name)

p = Person("patrick")
try:
    print(json.dumps(p))
except TypeError as err:
    print('ERROR:', err)


def custom_converter(obj):
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    d.update(obj.__dict__)
    return d


print("encoding Person:", json.dumps(p, default=custom_converter))


# Encoder,Decoder

def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print('MODULE:', module.__name__)
        class_ = getattr(module, class_name)
        print('CLASS:', class_)
        args = {
            key: value
            for key, value in d.items()
        }
        print('INSTANCE ARGS:', args)
        inst = class_(**args)
    else:
        inst = d
    return inst


encoded_object = '''
    [{"name": "instance value goes here",
      "__module__": "json_adv", "__class__": "Person"}]
    '''

myobj_instance = json.loads(
    encoded_object,
    object_hook=dict_to_object,
)
print(myobj_instance)