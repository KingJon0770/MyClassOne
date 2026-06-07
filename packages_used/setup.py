from setuptools import setup, find_packages

# 核心配置
setup(
    # 项目包名（pip安装时的名称）
    name="mydemotest",
    # 项目版本号
    # version="1.1.2",
    # 项目作者
    author="KingJon0770",
    # 作者邮箱
    author_email="18782541740@139.com",
    # 项目简介
    description="Python setup测试项目",
    # 项目主页地址,关键字段
    url="https://github.com/KingJon0770/MyClassOne/blob/master/packages_used/mydemotest",
    # 自动识别项目内所有包
    packages=find_packages(),
    # 兼容的Python版本
    python_requires=">=3.12",
)