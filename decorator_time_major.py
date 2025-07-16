'''
The process involves calculating the time taken before the operation starts, and then measuring how much time was consumed while performing the operation. This can be achieved using a decorator that tracks the execution time of the process.

Specifically:
Capture the start time before the operation begins.
Measure the time taken to perform the operation.
Output the total time taken for the process using a decorator.'''
from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func():
        t1 = time()
        result = func()
        t2 = time()
        print(f'Function {func.__name__} executed in {(t2-t1):.2}s')
        return result
    return wrap_func


@timer_func
#This is only operation
def Operation_func():
    for i in range(10):
        for j in range(100000):
            i*j

start_deco_time = time()
Operation_func()
print(f'Execute decorator time: {(time()-start_deco_time):.2}s')
