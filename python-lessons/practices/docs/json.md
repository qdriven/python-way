# Python Module - json
 
 json在http协议的调用中使用广泛，python自带的json库基本可以满足使用，json库主要的方法
 其实就这个两个：
 
 - dumps
 - loads
 
 # JSON dumps
 
 dumps 就是把python中的数据结构转换为json string
 
```python
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
```

结果如下：

```python
JSON:{"first": 1, "second": 3, "third": [12, 3, 4]}
<class 'str'> # 是个string 类型
```

# json loads

loads 方法把json字符串加载成为python对象(dict,list)都可以

```python
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
```

运行的结果是：

```python
{'key': 'value', 'key_map': {'nested': 'value'}, 'key_list': ['v1', 'v2', 'v3']}
<class 'dict'>
[{'k1': 'v1'}, {'k2': 'v2'}, {'k2': 'v2'}]
<class 'list'>
```

# json 如何dumps/loads 一个python的类

以上简单介绍了json的dumps和loads的方法，下面就有一个问题，是否可以直接dumps
一个python类到json字符串，或者loads json字符串创建制定类型的python类呢？
显然这肯定可以是的，那就动手试试。

- 定义一个类

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{{'name':'{}'}}".format(self.name)
```

- dumps Person instance

```python
p = Person("patrick")
try:
    print(json.dumps(p))
except TypeError as err:
    print('ERROR:', err)

```

结果是：

```python
ERROR: Object of type 'Person' is not JSON serializable
```

很显然不能直接dumps一个python的类，怎么办？使用dumps中的default参数
自定义一个转换的方法就可以了，

```python
p = Person("patrick")
def custom_converter(obj):
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    d.update(obj.__dict__)
    return d

print("encoding Person:", json.dumps(p, default=custom_converter))
```

结果是：

```python
encoding Person: {"__class__": "Person", "__module__": "__main__", "name": "patrick"}
```

这样就成功转化为JSON字符串了.

- loads

loads实际是dumps的相反过程，定一个dict to object 方法就可以，使用方法如下：

```python

## module name is json_adv, 同时Person 类在json_adv 文件中
def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print('MODULE:', module.__name__)
        class_ = getattr(module, class_name)
        print('CLASS:', class_)
        args = {
            key: value
            for key, value in d.items()
        }
        print('INSTANCE ARGS:', args)
        inst = class_(**args)
    else:
        inst = d
    return inst


encoded_object = '''
    [{"name": "instance value goes here",
      "__module__": "json_adv", "__class__": "Person"}]
    '''

myobj_instance = json.loads(
    encoded_object,
    object_hook=dict_to_object,
)
print(myobj_instance)

```

结果：

```python
[{'name':'instance value goes here'}]
```
