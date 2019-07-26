#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Base(object):
    def __init__(self):
        pass

    def print_name(self):
        print(self.__class__.__name__)


class Base1(Base):
    def __init__(self):
        pass

Base().print_name()
Base1().print_name()
