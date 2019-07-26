# -*- coding: utf-8 -*-
import inspect
import os

# cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe())[0])))
# print(cmd_folder)
import sys

print(inspect.currentframe())
file_path = inspect.getfile(inspect.currentframe())
print(file_path)

cmd_folder = os.path.realpath(file_path)
print(cmd_folder)
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
print(sys.path)
