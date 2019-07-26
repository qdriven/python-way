# -*- coding:utf-8 -*-

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]


for name,count in zip(names,letters):
    print(name)