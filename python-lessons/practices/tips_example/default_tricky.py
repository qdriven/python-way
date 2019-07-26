# -*- coding:utf-8 -*-
import json


def decode(data, default={}):
    """
    todo: please modify the default value to immutable
    :param data:
    :param default:
    :return:
    """
    try:
        return json.loads(data)
    except ValueError as e:
        print(e)
        return default


foo = decode("bad data")
foo['map'] = 'tst'
bar = decode("bad data")
bar['bar'] = 'tst'

print(foo == bar)  # True
