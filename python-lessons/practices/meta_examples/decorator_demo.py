import time
from functools import wraps


def time_that(func):
    @wraps(func)
    def wrapper(*arg,**kwargs):
        start = time.time()
        result = func(*arg,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return result
    return wrapper

@time_that
def sum_it(n):
    sum=0
    for i in range(n):
       sum+=i
    return sum
if __name__ == '__main__':
    print(sum_it(100))
    print(sum_it(1000))
