import time
from timeit import timeit

from MyMenus.core_code import core1

if __name__ == '__main__':
    """
    stmt=函数名 不能加 ()：加括号会立刻执行函数，把返回值传给 timeit，失去循环测试意义。
    number=10：代表代码总共运行 10 次，返回值为总耗时（秒）。
    globals=globals()：让 timeit 能找到当前作用域里的变量 / 模块。
    timer=time.perf_counter是目前 Python 推荐、精度最高的计时函数，统计纯代码运行时间（不含休眠）
    """
    print("开始")
    timeit(stmt=lambda: core1.func1(), number=10, globals=globals(), timer=time.perf_counter)
    # timeit(stmt="core1.func1()", number=10, globals=globals(), timer=time.perf_counter)

# from MyMenus import core_code
#
# if __name__ == '__main__':
#     print("开始")
#     core_code.func1()
