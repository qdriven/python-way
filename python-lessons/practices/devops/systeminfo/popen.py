# -*- coding: utf-8 -*-
from subprocess import PIPE

import psutil

p=psutil.Popen(["ls","-a","-l"],stdout=PIPE)

print(p)
print(p.name())
print(p.username())
# print(p.communicate())
result = p.communicate()
# print(result[0])
# print(result[1])
print(p.cpu_times())
