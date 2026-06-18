import asyncio


# 定义协程函数
async def hello(name):
    print(f"hello,{name}.")
    await asyncio.sleep(1)
    print(f"Bye,{name}")


# 协程函数调用方式
# asyncio.run(hello("men"))

# 自动获取/创建事件循环（永不报错）
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello("men"))

async def main0():
    await hello("men")


# 关键字await
async def compute(x, y):
    print(f"{x},{y}")
    await asyncio.sleep(2)
    return x + y


async def main1():
    res = await compute(3, 4)
    print(f"[res]:{res}")


# task对象
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main2():
    # 创建并发任务
    task1 = asyncio.create_task(say_after(1, "hell jom"))
    task2 = asyncio.create_task(say_after(2, "hell jack"))
    print("tasks is started")
    await task1  # 等待任务完成
    await task2


# 批量管理协程函数 gather和await
async def fetch_data(delay, data_id):
    await asyncio.sleep(delay)
    return f"DATA:{data_id}"


async def main3():
    """通过gather并发执行收集结果，收集结果是按顺序的"""
    # result= await asyncio.gather(
    #     fetch_data(1,1),
    #     fetch_data(2,2),
    #     fetch_data(3,3)
    # )
    # print(f"results:{result}")
    """通过await收集,收集结果没有规律"""
    tasks = [asyncio.create_task(fetch_data(1, 'A')),
             asyncio.create_task(fetch_data(2, "B")),
             asyncio.create_task(fetch_data(3, 'C'))]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for d in done:
        print(d.result())
    print(f"[done]:{done}")
    print(f"[pending]:{pending}")


# 进阶1，同步原语
# 便于协程之间的协作
# 互斥锁，保护共享资源，防止并发访问冲突
shared_counter = 0
lock = asyncio.Lock()


async def increment():
    global shared_counter
    # 获取锁
    async with lock:
        temp = shared_counter
        await asyncio.sleep(0.1)
        shared_counter = temp + 1


async def main5():
    # 启动10个协程，并且让协程之间并发修改变量
    await asyncio.gather(*[increment() for _ in range(10)])
    print(f"Final counter:{shared_counter}")


# Semaphore 信号量，控制并发数量，常常用于控制并发数量
async def limit_access(sem, resource_id):
    async with sem:
        print(f"Accessing resource:{resource_id}")
        await asyncio.sleep(2)
        print(f"Releasing resource:{resource_id}")


async def main6():
    # 控制并发数量为3
    sem = asyncio.Semaphore(4)
    print(f"sem:{sem},sem_type:{type(sem)}")
    # 启动10个协程
    await asyncio.gather(*[limit_access(sem, i) for i in range(10)])


if __name__ == "__main__":
    # asyncio.run(hello("men"))
    # asyncio.run(main0())
    # asyncio.run(main1())
    # asyncio.run(main2())
    # asyncio.run(main3())
    # asyncio.run(main5())
    asyncio.run(main6())
