# -*- coding:utf-8 -*-
import functools
import queue
import random
import threading
import time


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
