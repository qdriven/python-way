# Python Module - timeit

timeit 模块提供了一个衡量小段代码执行时间的方法，timeit模块主要有如下几个方法或者类：
- Timer: 计时器类
- timeit： 计时方法
- setup： 初始化


## Timer 用法

如下时一个最简单用法，主要包括：

- setup一次执行中只执行一次
- timeit 加上次数参数2之后用，会执行此方法2次，但是setup只会一次
- repeat 方法,repeat参数表示执行总的次数，number参数表示每次执行方法执行几次

参考下例：

```Python
t = timeit.Timer(stmt="print('print method')", setup="print('setup')")
print("TimeIt:")
print(t.timeit(number=2))

print("REPEAT:")
print(t.repeat(repeat=3, number=2))  
```

结果：

```Python
TimeIt:
setup
print method
print method
9.105002391152084e-06

REPEAT:
setup
print method
print method
setup
print method
print method
setup
print method
print method
[7.041991921141744e-06, 7.328999345190823e-06, 6.8060035118833184e-06]

```

## timeit 命令行使用方法

timeit可以在命令行中使用，使用方法如下： ``` python -m timeit <statement>```

```python

python -m timeit '"-".join(str(n) for n in range(100))' 
```

结果：

```python
10000 loops, best of 3: 40.3 usec per loop
```