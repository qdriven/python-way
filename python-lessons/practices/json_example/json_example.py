# -*- coding: utf-8 -*-
import json

data = {
    "first": 1,
    "second": 3,
    "third": [12, 3, 4]
}
"""
dump dict to json string
"""
print("JSON:{}".format(json.dumps(data)))
print(type(json.dumps(data)))

data_list = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print("DATA:", repr(data_list))
print("JSON:", json.dumps(data_list))
# convert json string back to python dict
json_str = """
{
    "key":"value",
    "key_map":{"nested":"value"},
    "key_list":["v1","v2","v3"]
}
"""
json_array = """
[{"k1":"v1"},{"k2":"v2"},{"k2":"v2"}]
"""
# load json
result = json.loads(json_str)
result1 = json.loads(json_array)
print(result)
print(type(result))
print(result1)
print(type(result1))



