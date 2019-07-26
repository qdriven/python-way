# Python Module - bisect

bisect 模块是可以保持list排序顺序的一个模块，通过以下两个例子可以清楚的了解：

- insort or insort_right

```python
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

# insort, insert a data into a sorted list while maintaining the list in sorted
l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3}  {:3}'.format(i, position), l)
```

- insort_left 例子

```python
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3}  {:3}'.format(i, position), l)
```

两个例子的结果比较一下可以看到：

```
insort,insort_right:
 77    8 [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]

insort_left:
 77    7 [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]

```

insort_left 插入位置为7，这个就是insert,insert_right插入位置为8