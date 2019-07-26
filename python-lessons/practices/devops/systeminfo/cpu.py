# -*- coding: utf-8 -*-

import psutil



"""
User Time
System Time
Wait IO
Idle
irq
softirq
nice
"""
cpu_times = psutil.cpu_times()
cpu_times1 = psutil.cpu_times(percpu=True)
print(cpu_times,cpu_times1)
print(psutil.cpu_count(logical=False))  ## CPU Processor
print(psutil.cpu_count())  ## CPU Processor