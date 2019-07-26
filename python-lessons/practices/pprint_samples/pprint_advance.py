# -*- coding:utf-8 -*-
from pprint import pprint

from pymodules.pprint import data

pprint(data, depth=1)
pprint(data, depth=2)


for width in [80, 5]:
    print('WIDTH =', width)
    pprint(data, width=width)
    print()

print('DEFAULT:')
pprint(data, compact=False)
print('\nCOMPACT:')
pprint(data, compact=True)