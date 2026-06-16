
from functools import wraps
import time
"""
装饰器：
1. 装饰器是一种函数，它可以让其他函数在不修改源代码的前提下增加额外功能。
2. 装饰器的语法糖@wraps(func)可以保留原函数的元信息，使得装饰器可以像原函数一样被调用。
3. 装饰器可以接收函数作为参数，并返回一个新的函数。
4. 装饰器可以用在函数、类、方法上。
5. 装饰器可以用在函数调用前后、函数异常时、函数返回值时等多个场景。
6. 装饰器可以用在复杂的场景中，比如：日志、缓存、权限校验、事务处理等。
"""

def decorator_timer(func):
    """
    装饰器：函数运行计时器
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}开始运行...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__}运行结束...")
        print(f"{func.__name__}运行时间：{end_time - start_time:.3f}s")
        return result
    return wrapper

class DecoratorClass:
    def __init__(self, func):
        self.func = func

    # 如果是装饰器器类，必须要重写__call__函数
    def __call__(self, *args, **kwargs):
        print(f"{self.func.__name__}开始运行...")
        start_time = time.perf_counter()
        self.func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{self.func.__name__}运行结束...")
        print(f"{self.func.__name__}运行时间：{end_time - start_time:.3f}s")
        # return self.func(*args, **kwargs)