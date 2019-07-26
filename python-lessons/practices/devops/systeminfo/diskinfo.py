# -*- coding: utf-8 -*-
import psutil
# disk usage for root
print(psutil.disk_usage('/'))
# disk partitions
print(psutil.disk_partitions())

print(psutil.disk_io_counters(perdisk=True))
print(psutil.disk_io_counters())
