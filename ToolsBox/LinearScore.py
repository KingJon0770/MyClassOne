def linear_score(actual_value: float, max_index: float, min_index: float, max_score: float, min_score:float):
    """
    线性得分计算公式（等比例得分）
    :param actual_value: 实际完成值（你要计算得分的数值）
    :param max_index: 指标最大值（达到这个值得满分）
    :param min_index: 指标最小值（达到这个值得最低分）
    :param max_score: 满分,默认100分
    :param min_score: 最低分,默认0分
    :return: 计算后的得分(保留2位小数)
    """
    # 防止分母为0（最大值=最小值时直接返回满分）
    if max_index == min_index:
        return round(max_score, 2)
    
    # 实际值超过最大值 → 得满分
    if actual_value >= max_index:
        return round(max_score, 2)
    
    # 实际值低于最小值 → 得最低分
    if actual_value <= min_index:
        return round(min_score, 2)
    
    # 核心线性得分公式
    score = min_score + (max_score - min_score) * (actual_value - min_index) / (max_index - min_index)
    
    # 保留2位小数返回
    return round(score, 2)



if __name__ == '__main__':
    print("===== 线性得分计算器 =====")
    # 1. 自定义你的指标规则
    max_index = 90    # 指标最大值（例：完成100件得满分）
    min_index = 60      # 指标最小值（例：完成0件得最低分）
    max_score = 20    # 满分
    min_score = 10      # 最低分

    # 2. 输入实际值
    try:
        actual = float(input("请输入实际完成值："))
        # 3. 计算得分
        result = linear_score(actual, max_index, min_index, max_score, min_score)
        # 4. 输出结果
        print(f"\n指标范围：{min_index} ~ {max_index}")
        print(f"得分范围：{min_score} ~ {max_score}")
        print(f"实际完成值：{actual}")
        print(f"最终得分：{result} 分")
    except ValueError:
        print("输入错误！请输入数字。")