# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     string_demo
   Description :  https://www.tutorialspoint.com/python/python_strings.htm
   Author :        patrick
   date：          2019/7/9
-------------------------------------------------
   Change Activity:
                   2019/7/9:
-------------------------------------------------
"""
__author__ = 'patrick'

var1 = "Hello World"
var2 = "Hello Python"

print("formatting--string")
print("%s,%s" % ("Hello", "World"))
print("{},{}".format("Hello", "world"))
print("{hello}".format(hello="Hello"))

print("string slice")
print("Hello"[0])
print("Hello"[1:3])

print("string operator")
print("e" not in "Hellp")

print("row string")
print(r"c://test")

print("string built-in function")
print("hello".capitalize())
print("Hello".count("l"))

print("start_with".startswith("s"))
print("start_with".endswith("h"))
print("baidu.com".find("ont"))  # -1
print("hello".index("e"))

##a lot of functions
