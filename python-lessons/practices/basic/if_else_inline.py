#!/usr/bin/env python
# -*- coding: utf-8 -*-

def if_else_inline(key):
    return 'method' if key == 'test' else 'testing'


print(if_else_inline("test"))
print(if_else_inline("1test"))
