# -*- coding:utf-8 -*-
import csv

import MySQLdb

# pool = ThreadPool(10)
from csv_example import c

count = 0
with open('cardmlist.csv', 'r') as f:
    for row in csv.reader(f, delimiter=","):
        cardid = row[0]

        c.execute("select * from card_m_list where cardid = '{}'".format(cardid))
        result = c.fetchone()
        count += 1
        print(count)
        if result is None:
            print(cardid)
