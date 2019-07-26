# -*- coding: utf-8 -*-
import csv

data = [["first",1,23],["second",5,5678]]

with open("example.csv",'w') as f:
    writer = csv.writer(f,delimiter=';',quotechar='"')
    writer.writerows(data)


with open('example.csv','r') as f:
    for row in csv.reader(f,delimiter=";"):
        print(row)