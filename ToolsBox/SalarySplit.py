def salary_split(salary, denominations=[100, 50, 20, 10, 5, 2, 1]):
    """
    递归函数：工资按面额配钞（最少张数，从大到小拆分）
    :param salary: 工资金额（整数）
    :param denominations: 面额列表，默认按你表格顺序
    :return: 各面额列表（与面额一一对应）
    """
    # 递归终止条件：没有面额了，返回空列表
    if not denominations:
        return []

    # 取当前最大面额
    current = denominations[0]
    # 计算当前面额的张数
    count = salary // current
    # 计算剩余需要拆分的工资
    remain = salary % current

    # 递归：处理剩余金额 + 剩下的面额
    return [count] + salary_split(remain, denominations[1:])


def salary_split2(salary, denoms=[100, 50, 20, 10, 5, 2, 1]):
    """
    纯递归工资配钞函数（无循环）
    """
    # 递归终止：面额用完，返回空
    if not denoms:
        return []

    # 当前面额张数 + 剩余金额递归
    return [salary // denoms[0]] + salary_split2(salary % denoms[0], denoms[1:])


# ===================== 测试你的数据 =====================
if __name__ == '__main__':
    # 员工数据
    print(salary_split(4744))
    print(salary_split2(4744))
