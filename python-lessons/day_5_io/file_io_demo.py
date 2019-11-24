# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     file_io_demo
   Description :
   Author :        patrick
   date：          2019/11/24
-------------------------------------------------
   Change Activity:
                   2019/11/24:
-------------------------------------------------
"""
import base64

__author__ = 'patrick'

with open('test.jpg', 'rb') as im_reader:
    image_data = im_reader.read()
    base64_data = base64.b64encode(image_data)  # 使用 base64 编码
    print(base64_data)
