def write_file(filename,data):
    """
    写文件
    :param filename:文件名
    :return: 返回写结果
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            return f.write(data)
    except Exception as e:
        print(f'写文件异常,e is ：{e}')
        return None
