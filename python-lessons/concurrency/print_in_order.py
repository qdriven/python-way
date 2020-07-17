# encoding: utf-8

"""
link: https://leetcode-cn.com/problems/print-in-order/
Condition Lock Semaphore Barrier Event Queue
"""
import queue
import threading
from typing import Callable


class FooGlobalIndicator:
    """
    Set a Global Indicator for Concurrent Indicator
    """

    def __init__(self):
        self.indicator = 0

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.indicator = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        while self.indicator != 1:  ## waiting for the indicator change
            pass
        printSecond()
        self.indicator = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        while self.indicator != 2:
            pass
        printThird()


"""
TODO: error to fix
"""


class FooCondition:
    """
    Set a Global Indicator for Concurrent Indicator
    """

    def __init__(self):
        self.c = threading.Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.run_if_runnable(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.run_if_runnable(1, printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.run_if_runnable(2, printThird)

    def run_if_runnable(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda: val == self.t)  # 参数是函数对象，返回值是bool类型
            func()
            self.t += 1
            self.c.notify_all()


class FooLock:

    def __init__(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        self.l2 = threading.Lock()
        self.l2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.l1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        printSecond()
        self.l2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        printThird()


class FooSemaphore:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        printThird()


class FooEvent:
    def __init__(self):
        self.b1 = threading.Event()
        self.b2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()


class FooBarrier:
    def __init__(self):
        self.b1 = threading.Barrier(2)
        self.b2 = threading.Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()


class FooQueue1:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()


class FooQueue2:
    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q1.put(0)
        self.q2 = queue.Queue(1)
        self.q2.put(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.get()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.put(0)
        printSecond()
        self.q2.get()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.put(0)
        printThird()


class FooDict:
    """
    Lazy Running
    """
    def __init__(self):
        self.d = {}

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.d[0] = printFirst
        self.res()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.d[1] = printSecond
        self.res()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.d[2] = printThird
        self.res()

    def res(self) -> None:
        if len(self.d) == 3:
            self.d[0]()
            self.d[1]()
            self.d[2]()
