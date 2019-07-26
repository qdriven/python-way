# -*- coding:utf-8 -*-
import queue

q = queue.Queue()

for i in range(5):
    q.put(i)
# first in first out
while not q.empty():
    print(q.get(), end=' ')
print()

# LIFO QUEUE, last in first out queue

lifoQueue = queue.LifoQueue()
for item in range(5):
    lifoQueue.put(item)

while not lifoQueue.empty():
    print(lifoQueue.get(), end=' ')
print()


