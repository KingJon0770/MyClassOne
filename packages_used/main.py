from mypackage import reader, writer


def main():

    write_lens = writer.write_file('data.txt', '这是全栈学习资料')
    # 写入失败直接返回
    if not write_lens:
        return
    # 写入成功
    print("写入成功")

    data = reader.read_file('data.txt')
    # 读取失败直接返回
    if not data:
        print("读取文件失败")
        return
    print(f"读取文件成功，读取的数据为：{data}")



if __name__ == '__main__':
    main()
