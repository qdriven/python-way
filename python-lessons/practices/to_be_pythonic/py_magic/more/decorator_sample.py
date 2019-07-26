# -*- coding: utf-8 -*-
import logging
import time
from functools import wraps

logging.basicConfig(format='[%(asctime)s](%(filename)s#%(lineno)d)%(levelname)-7s %(message)s',
                    level=logging.DEBUG)


def calculate_time(func):
    @wraps(func)
    def timer(*args, **kwargs):
        for item in args:
            logging.info(item)
        for item in kwargs:
            logging.info(kwargs[item])
        start_at = time.time()
        logging.info("timer starting.......")
        actual_result = func(*args, **kwargs)
        end_at = time.time()
        logging.info(end_at - start_at)
        return actual_result

    return timer


@calculate_time
def some_slow_function(interval=1):
    time.sleep(interval)
    return "slow function"


some_slow_function(interval=2)


class intercept_me(object):
    def __init__(self, func):
        self.func = func
        logging.info(id(self))

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@intercept_me
def new_func():
    print("this is testing")
