# Python Magic Method

Pytho内建有```__init__```这样的方法被称为魔术方法(magic method),常用的魔术方法如下:
- `__new__`
- `__str__` , `__repr__`
- `__iter__`
- `__getitem__` , `__setitem__` , `__delitem__`
- `__getattr__` , `__setattr__` , `__delattr__`
- `__call__`
- `__init__`

## `__new__` 方法使用

`__new__` 实际上在调用`__init__`之前就会使用, 这个实验可以清楚的展示:

```python
class MagicMethodClass:

    @property
    def __class__(self: Any) -> Type[Any]:
        return super().__class__()

    def __new__(cls) -> Any:
        print("this is in __new__ method .....")
        return super().__new__(cls)

    def __init__(self):
        print("this is from init method")

if __name__ == '__main__':
    magic_method = MagicMethodClass()
```