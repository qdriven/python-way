import json


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)


class Struct(Person):
    def __init__(self, **entries):
        self.__dict__.update(entries)





if __name__ == '__main__':
    p = Person("name", age="age")
    print(p.to_dict())

    print(p.__dict__)
    print(p.to_json())
    d = {"name1": "name", "age1": 12}
    s = Struct(**d)
    print(s.to_dict())
    print(s.to_json())
    print(s.name1)
    print(s.age1)
    print(vars(s))
    print(vars())