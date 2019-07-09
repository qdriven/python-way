# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     process_time
   Description :
   Author :        patrick
   date：          2019/6/28
-------------------------------------------------
   Change Activity:
                   2019/6/28:
-------------------------------------------------
"""
__author__ = 'patrick'

result = []
with open('process_time.txt','r') as pt:
    lines = pt.readlines()
    for line in lines:
        process_time = line.split(" ")[-1].replace("\n","")
        if int(process_time)>2:
            result.append(int(process_time))

average_process_time = sum(result)/len(result)
print(average_process_time)
