# -*- coding: utf-8 -*-
import psutil

print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))
# print(psutil.net_connections())
print(psutil.net_io_counters())