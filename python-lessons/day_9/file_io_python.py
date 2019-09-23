# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     file_io_python
   Description :
   Author :        patrick
   date：          2019/9/22
-------------------------------------------------
   Change Activity:
                   2019/9/22:
-------------------------------------------------
"""
import turtle

__author__ = 'patrick'

"""
Read Single line
Read Multiple Line
"""
def main():
    file_name = "test.txt"
    t = turtle.Turtle()
    screen = t.getscreen()
    with open(file_name, 'r') as file:
        for line in file:
            print(line)

if __name__ == '__main__':
    main()
