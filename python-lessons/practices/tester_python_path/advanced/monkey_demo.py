# -*- coding: utf-8 -*-
from tester_python_path.advanced.monkey import MonkeyPatch


def get_info(self,*args):
    return "monkey patch"

MonkeyPatch.get_info=get_info

monkey = MonkeyPatch()
print(monkey.get_info("test"))
