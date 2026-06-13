from functools import cache

from ..tool_code.GetRunTimer import get_run_time


@get_run_time
@cache
def func1():
    total = 0
    for i in range(1000000):
        total += i
    print(total)
    return total
