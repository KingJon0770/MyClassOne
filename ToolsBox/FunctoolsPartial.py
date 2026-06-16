from functools import partial


def specifications(color: str, name: str, amount: int):
    """
    重复调用函数时，可以传入部分参数，返回一个新的函数，可以传入剩余参数
    """
    print(f'Spaces:{color = }, {name = }, {amount = }')


color_and_name_spaces: partial = partial(specifications, amount=10)  # 传入最后一个
specify_amount = partial(specifications, "blue", "Bob")
specify_name = partial(specifications, "blue", amount=10)  # 传入第一个和最后一个

if __name__ == '__main__':
    color_and_name_spaces('Red', 'Bob', amount=15)  # 关键字参数重新传值也是可以的，不传代表默认
    color_and_name_spaces('Red', 'Bob')
    specify_amount(10)
    specify_name("Lilei")
    specify_name("Lilei",amount=5)
