# -*- coding: utf-8 -*-
import psutil

# getting running pids
print(psutil.pids())

# Process for single process
print(psutil.Process(psutil.pids()[0]))

for pid in psutil.pids():
    p = psutil.Process(pid)
    if isinstance(p, psutil.ZombieProcess):
        # print(p)
        # print(p.status())
        pass
    else:
        print(p.uids())
        print(p.cwd())
        # print(p.exe())
        print(p.cpu_times())
        print(p.num_threads())