from loguru import logger
from GetLogger import init_logger

init_logger()

@logger.catch(reraise=True)
def main(file):
    # logger.debug("调试信息")
    # logger.info("服务启动成功")
    # logger.warning("这是一条警告")
    # logger.error("业务异常")
    # # 测试异常
    # 1 / 0
    get_dd(file)

def get_dd(file):
    logger.info(f'{file}')
if __name__ == "__main__":
    file=r'路径'
    main(file)