# -*- coding:utf-8 -*-


import subprocess

try:
    print(subprocess.run(['false']))
    print(subprocess.run(['false'],check=True))
except subprocess.CalledProcessError as err:
    print('ERROR:', err)