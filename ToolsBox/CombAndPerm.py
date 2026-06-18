from itertools import combinations_with_replacement, permutations,product

def permutations_example() -> None:

    """
    实现不重复排序的功能，不可以重复
    """
    elements: list[str] = ['A', 'B', 'C']
    perms: permutations[str] = permutations(elements,3) # 第二个参数代表是返回是几个值的排列方式
    return list(perms)
    """
    A C B
    B A C
    B C A
    C A B
    C B A
    """

def combinations_example() -> tuple[tuple[str]]:
    """
    实现重复排序的功能，可以重复
    """
    elements: list[str] = ['A', 'B', 'C']
    combs = combinations_with_replacement(elements, 3)  # 第二个参数代表是返回是几个值的组合方式
    return list(combs)

    """
    [('A', 'A', 'A'),
    ('A', 'A', 'B'), 
    ('A', 'A', 'C'), 
    ('A', 'B', 'B'), 
    ('A', 'B', 'C'), 
    ('A', 'C', 'C'), 
    ('B', 'B', 'B'), 
    ('B', 'B', 'C'), 
    ('B', 'C', 'C'), 
    ('C', 'C', 'C')]
    """
def product_example()-> list[tuple[list[str]]]:
    """
    实现笛卡尔积的功能，可以重复
    """
    elements: list[list[str]] = [['A','B'], ['C', 'D']]
    my_product: product = product(elements, repeat=2)
    return list(my_product)
    """
    [(['A', 'D'], ['A', 'D']), 
    (['A', 'D'], ['B', 'C']), 
    (['B', 'C'], ['A', 'D']),
    (['B', 'C'], ['B', 'C'])]
    """

if __name__ == '__main__':
    print(permutations_example())
    print(combinations_example())
    print(product_example())