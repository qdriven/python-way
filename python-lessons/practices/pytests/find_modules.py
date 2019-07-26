#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
import inspect

modules = importlib.__import__('sample_data')
members = inspect.getmembers(modules)
for member in members:
    if not member[0].startswith("__"):
        print(member)

