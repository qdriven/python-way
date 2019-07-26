# -*- coding:utf-8 -*-
import pkgutil
from pprint import pprint

pprint(__file__)
pprint(__package__)

__path__ =pkgutil.extend_path(__file__,'extension')

pprint(__path__)