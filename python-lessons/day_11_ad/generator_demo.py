# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     generator_demo
   Description :
   Author :        patrick
   date：          2019/11/24
-------------------------------------------------
   Change Activity:
                   2019/11/24:
-------------------------------------------------
"""
__author__ = 'patrick'


def generator_func():
    yield 1
    yield 2
    yield 3


g = generator_func()
print(next(g))
print(next(g))
g.close()
print(next(g))

"""
- [Python yield 使用浅析](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)
- [谈谈Python的生成器 – 思诚之道](http://www.bjhee.com/python-yield.html)
- [Function vs Generator in Python](https://code-maven.com/function-vs-generator-in-python)
- [Lazy Method for Reading Big File in Python? - Stack Overflow](http://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python)
"""
