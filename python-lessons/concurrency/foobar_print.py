# encoding: utf-8
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.full_sign = threading.Semaphore(0)
        self.ready_sign = threading.Semaphore(1)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.ready_sign.acquire
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.full_sign.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.full_sign.acquire()
            printBar()
            self.ready_sign.release()


class FooBarDict():
    def __init__(self, n):
        self.n = n
        self.funcMap = {}

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.funcMap['f'] = printFoo
            self.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.funcMap['b'] = printBar
            self.release()

    def release(self):
        if len(self.funcMap) == 2:
            for i in range(self.n):
                self.funcMap['f']()
                self.funcMap['b']()
