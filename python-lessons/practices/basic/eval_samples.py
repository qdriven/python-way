#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import dpath

text_context = {}
text_samples = {
    "name": text_context.get("name")
}
print(text_samples)

text_context["categoryId"] = "test"

print(eval(str(text_samples)))

result = {"params": {"categoryId": "_categoryId",
                     "update": {"id": "_categoryId",
                                "name": "测试分类修改", "description": "测试描述修改",
                                "restaurantId": "abcds", "createdTime": 1462358554, "foodCount": 0,
                                "valid": True, "readonly": False}}}

# result[("params","update","id")]="5"
paths= "params.categoryId".split('.')
path = '['+']['.join(paths)+']'
print(path)

dpath.util.set(result,'params/categoryId',"990")
dpath.util.set(result,'params/update/id',"990")
print(result)

