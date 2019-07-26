# -*- coding: utf-8 -*-
from copy import deepcopy

source = {
    "result": [{"activeTime": 1234543453, "id": 123}, {"activeTime": 34543453, "id": 123}]
}

source_1 = deepcopy(source)

result_1 = source.get('result')
result_2=sorted(source.get('result'),key=lambda item:item['activeTime'],reverse=True)
print(result_2)
print(type(result_1))
# key is lambda, a function
result_1.sort(key=lambda item: item['activeTime'], reverse=True)
print(result_1)
assert source.get('result') == result_1
# print(result_1)
assert source.get('result') == sorted(source.get('result'),key=lambda item:item['activeTime'],reverse=True)
