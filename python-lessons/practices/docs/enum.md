# Python Module - enum

enum module可以用来很好的定义一个可以迭代和比较的类型.
下面主要介绍enum的

- create 创建
- iteration 迭代
- complex enum value 复杂enum值

## 创建enum

- 继承enum.Enum就可以

```python
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1
```

运行如下程序就可以查看enum的值：

```python
print('Member name: {},Member value: {}'.format(BugStatus.wont_fix, BugStatus.wont_fix.value))
```

- 自定义enum.Enum

```python
BugStatusP = enum.Enum(
    value="BugStatusP",
    names=('a b c d e')
)

```

运行如下程序可以查看enum的值：

```python

for status in BugStatusP:
    print("{:15}={}".format(status.name, status.value))
```

## enum iteration

enum 可以理解为类似于name和value的一个dict，所以使用如下方法可以遍历迭代：

```python

for status in BugStatus:
    print("{:15}={}".format(status.name, status.value))
```

## 复杂的enum value类型

enum的value可以是一个复杂的值，如下例：

```python
class BugStatusC(enum.Enum):

    new = {
        'num': 7,
        'transitions': [
            'incomplete',
            'invalid',
            'wont_fix',
            'in_progress',
        ],
    }
    incomplete = {
        'num': 6,
        'transitions': ['new', 'wont_fix'],
    }
    invalid = {
        'num': 5,
        'transitions': ['new'],
    }
    wont_fix = {
        'num': 4,
        'transitions': ['new'],
    }
    in_progress = {
        'num': 3,
        'transitions': ['new', 'fix_committed'],
    }
    fix_committed = {
        'num': 2,
        'transitions': ['in_progress', 'fix_released'],
    }
    fix_released = {
        'num': 1,
        'transitions': ['new'],
    }

    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']

    def can_transition(self, new_state):
        return new_state.name in self.transitions

print('Name:', BugStatusC.in_progress)
print('Value:', BugStatusC.in_progress.value)
print('Custom attribute:', BugStatusC.in_progress.transitions)
print('Using attribute:',
      BugStatusC.in_progress.c
```

这个例子中 enum的一个value实际上一个dict，包含了相对比较复杂的数据结构

但是无论如何变化，可以将enum总结了

1.类似一个dict
2.可以直接通过enum的name访问预定义name的值
3.和dict一样可以遍历

