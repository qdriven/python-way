# -*- coding: utf-8 -*-
import datetime

import psutil

print(psutil.users())
users = psutil.users()

print(users[0].host)
print(users[0].terminal)
print(users[0])
print(type(users[0]))
print(users[1].name)
print(users[1].terminal)
print(datetime.datetime.fromtimestamp(users[1].started))

