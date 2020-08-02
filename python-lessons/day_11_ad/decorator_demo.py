"""
Decorator in Python
1. Simple Decorator
2. Build Decorator
3. Decorator Class Usage
"""

# defining a decorator
import math
import time
from functools import wraps


def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
        # calling the actual function now
        # inside the wrapper function.
        func()
        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)


## Case 1: calculate time

def calculate_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("total time used in :", func.__name__, args, end - begin)

    return inner


@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


print(factorial.__name__)
factorial(2)
factorial(10)
