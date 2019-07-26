# -*- coding:utf-8 -*-

def try_to_change(str):
    str = "Hell STR"


name = "patrick"

## string is immutable
try_to_change(name)
print(name)


def try_to_change_mutable(mutable):
    if isinstance(mutable, list):
        return mutable.append("test")
    if isinstance(mutable, dict):
        return mutable.update(key="key", value="value")


# list and dict is updated,they are mutable
mutable_list = ['123', 324]
mutable_dict = {"k1": "v1", "k2": "v2"}
try_to_change_mutable(mutable_list)
print(mutable_list)
try_to_change_mutable(mutable_dict)
print(mutable_dict)
