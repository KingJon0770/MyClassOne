import time

from functools import wraps
from typing import Callable, Any


def get_run_time(func: Callable) -> Callable:
    """
    装饰器，用于计算函数运行时间
    :param func: 被装饰的函数
    :return: 装饰后的函数
    """
    @wraps(func)
    def func_wrapper(*args, **kwargs) -> Any:
        stat = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"运行{func.__name__}耗时：{end - stat:.3f}秒")

    return func_wrapper

# @get_run_time
# def main():
#     print("hello world")
#
#
# if __name__ == '__main__':
#     main()
