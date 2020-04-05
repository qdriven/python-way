# -*- coding:utf-8 -*-

def get(path):
    print(path)


def put(path):
    print("put " + path)


def post(path):
    print("post " + path)


method_map = {
    "GET": get,
    "POST": post,
    "put": put,
}


class ObjectHolder:
    def __init__(self):
        pass

    def __getattr__(self, item):
        return method_map.get(item.upper())


ObjectHolder().get("test")
