# -*- coding:utf-8 -*-
import csv

from csv_example import c

result = []
with open('cardmlist.csv', 'r') as f:
    for row in csv.reader(f, delimiter=","):
        cardid = row[0]
        result.append(cardid)

c.execute("select * from card_m_list where ignite_update_time>0")

result_db = c.fetchall()
result_all = []
# print(result_db)

for item in result_db:
    result_all.append(item[0])

for item in result:
    if item not in result_all:
        print(item)
