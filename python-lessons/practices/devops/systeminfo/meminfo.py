# -*- coding: utf-8 -*-

"""
1. Free
2. total,used,free,buffers,cache,swap
"""
import psutil

mem = psutil.virtual_memory()
print(psutil.swap_memory())
print(psutil.virtual_memory())
## free -m | grep Mem | awk '{print $2}'
print(mem.total)
## free -m | grep Mem | awk '{print $3}'
print(mem.used)