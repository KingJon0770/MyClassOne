import sys
from pathlib import Path
from loguru import logger

def init_logger(
    log_dir: str = "logs",
    console_level: str = "INFO",
    file_level: str = "DEBUG",
    json_log: bool = True
):
    # 清空默认配置
    logger.remove()

    # 创建日志目录
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    # 1. 控制台输出（彩色、简洁）
    logger.add(
        sink=sys.stderr,
        level=console_level,
        colorize=True,
        format="<cyan>{time:MM-DD HH:mm:ss}</cyan> | <level>{level:8}</level> | {message}",
        enqueue=True,
    )

    # 2. 普通文件日志（按天切割、保留30天、自动压缩）
    logger.add(
        sink=f"{log_dir}/app_{{time:YYYY-MM-DD}}.log",
        level=file_level,
        rotation="00:00",        # 每天零点切割
        retention="30 days",      # 保留30天
        compression="zip",        # 旧日志压缩
        encoding="utf-8",
        enqueue=True,             # 多进程/线程安全
        diagnose=False,           # 生产关闭详细变量泄露
    )

    # 3. JSON结构化日志（方便对接 ELK、 Loki、监控）
    # if json_log:
    #     logger.add(
    #         sink=f"{log_dir}/app_json_{{time:YYYY-MM-DD}}.log",
    #         level=file_level,
    #         rotation="00:00",
    #         retention="30 days",
    #         compression="zip",
    #         encoding="utf-8",
    #         enqueue=True,
    #         serialize=True,       # JSON格式
    #     )

# 初始化日志
init_logger()

# 全局异常捕获装饰器（放在入口函数上即可）
@logger.catch(reraise=True)
def main():
    logger.debug("调试信息")
    logger.info("服务启动成功")
    logger.warning("这是一条警告")
    logger.error("业务异常")
    # 测试异常
    1 / 0

if __name__ == "__main__":
    main()