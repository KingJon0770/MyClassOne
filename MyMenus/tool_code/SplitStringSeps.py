def split_string_seps(ss, seps):
    # 将字符串放入列表中
    res_list: list = list([ss])
    # 通过列表.extend方式添加列表到列表中
    for sep in seps:
        lst_extend = []
        list(map(lambda x: lst_extend.extend(str(x).split(sep)), res_list))
        res_list = lst_extend
    return res_list


if __name__ == '__main__':
    sss = "dddd=dd,cc=12,12,21=13"
    print(split_string_seps(sss, '=,'))
