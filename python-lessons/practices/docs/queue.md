# Python Module - queue

queue提供了一些不同的Queue的实现的实现，包括如下内容：

- Queue(first in,first out)
- LifoQueue (last in ,first out)
- PriorityQueue

## Queue, first in first out

python Queue是一个FIFO的queue实现，可以参考如下代码可以清楚的看出FIFO：

```python

q = queue.Queue()

for i in range(5):
    q.put(i)
# first in first out
while not q.empty():
    print(q.get(), end=' ')
print()
```

结果如下：FIFO

```
0 1 2 3 4
```

## LIFOQueue- Last In,First Out

LIFOQueue是一个Last In First out的实现，参考如下代码：

```python
lifoQueue = queue.LifoQueue()
for item in range(5):
    lifoQueue.put(item)

while not lifoQueue.empty():
    print(lifoQueue.get(), end=' ')
print()
```

结果如下：

```
4 3 2 1 0
```

## PriorityQueue

PriorityQueue根据优先级来从队列取出数据. 下面是关于PriorityQueue的一些示例代码，这些代码包括如下几个部分：

- 一个自定义的放入PriorityQueue的Job，需要比较Priority
- 多线程执行任务，根据Priority来执行任务

1. 定义JOB，同时将JOB放入PriorityQueue中：

```python

@functools.total_ordering
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()
q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level-10 job'))
q.put(Job(20, 'Low-level-20 job'))
q.put(Job(1, 'Important job'))
```

2. 执行Queue中的任务


```python

def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        print(random.randint(1, 10))
        time.sleep(random.randint(1, 10))
        q.task_done()


workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,))
]

for worker in workers:
    worker.setDaemon(True)
    worker.start()

q.join()
```

结果：可以从结果看到Import到Low-Level按优先级执行任务

```
Processing job: Important job
2
Processing job: Mid-level job
9
Processing job: Low-level-10 job
8
Processing job: Low-level-20 job
7
```


