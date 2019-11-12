# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     class_magic_methods
   Description :
   Author :        patrick
   date：          2019/11/11
-------------------------------------------------
   Change Activity:
                   2019/11/11:
-------------------------------------------------
"""
from typing import Iterable, Any, Type

__author__ = 'patrick'


class MagicMethodClass:
    _instance_dict = dict()

    @property
    def __class__(self: Any) -> Type[Any]:
        print("class name")
        return super().__class__()

    def __new__(cls) -> Any:
        print("this is in __new__ method .....")
        if len(MagicMethodClass._instance_dict) > 0:
            print("return existing instance")
            return MagicMethodClass._instance_dict[0]
        else:
            print("new object")
            return object.__new__(cls)

    def __init__(self):
        print("this is init")
        print("init")
        MagicMethodClass._instance_dict[0] = self
        print(MagicMethodClass._instance_dict[0])
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
    ## python3 __next__
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __setattr__(self, name: str, value: Any) -> None:
        print("this is set attr method ....")
        super().__setattr__(name, value)

    def __eq__(self, o: object) -> bool:
        print("this is eq method ....")
        return super().__eq__(o)

    def __ne__(self, o: object) -> bool:
        return super().__ne__(o)

    def __str__(self) -> str:
        return __file__

    def __repr__(self) -> str:
        return super().__repr__()

    def __hash__(self) -> int:
        return super().__hash__()

    def __format__(self, format_spec: str) -> str:
        return super().__format__(format_spec)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __delattr__(self, name: str) -> None:
        super().__delattr__(name)

    def __sizeof__(self) -> int:
        return super().__sizeof__()

    def __reduce__(self) -> tuple:
        return super().__reduce__()

    def __reduce_ex__(self, protocol: int) -> tuple:
        return super().__reduce_ex__(protocol)

    def __dir__(self) -> Iterable[str]:
        return super().__dir__()

    def __init_subclass__(cls) -> None:
        print("init sub class")
        super().__init_subclass__()


if __name__ == '__main__':
    magic_method = MagicMethodClass()
    print(id(magic_method))
    m2 = MagicMethodClass()
    print(id(m2))
    print(repr(m2))
    for i in m2:
        if i>10:
            break
        print(i)
    print(next(m2))