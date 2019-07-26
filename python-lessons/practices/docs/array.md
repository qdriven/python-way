# Python Module - Array

Array 模块定义了一个类似list的数据结构,这个模块支持的数据类型如下：

```
Code	Type	Minimum size (bytes)
b	int	1
B	int	1
h	signed short	2
H	unsigned short	2
i	signed int	2
I	unsigned int	2
l	signed long	4
L	unsigned long	4
q	signed long long	8
Q	unsigned long long	8
f	float	4
d	double float	8
```

## Init Array

初始化Array比较简单，定义array的存储类型和初始化值就可以：

```python
s = b'this is the array'
a = array.array('b', s)
```

## Array 数据操作

Array 的操作基本和python原始的array一样，包括了extend，slice等

```python
nums = array.array('i', range(3))
print("Initial {}".format(nums))
nums.extend(range(10))
print("after extend{}".format(nums))
print("slice {}".format(nums[2:5]))
print('Iterator: {}'.format(list(enumerate(nums))))
```

