import os


def dir_file_key(folder_path, keyword=None):
    # 检查目标文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 {folder_path} 不存在！")
        return print(f"错误：文件夹 {folder_path} 不存在！")

    # 切换文件路径到目标文件夹
    os.chdir(folder_path)
    for file_name in os.listdir():
        # 条件1：文件名包含指定关键词；条件2：文件后缀是.csv（忽略大小写）
        if file_name.endswith((".csv", ".xlsx")):
            if keyword in file_name:
                # 拼接完整文件路径
                file_match = os.path.join(folder_path, file_name)
                return file_match
    return None


# ------------------- 调用示例 -------------------
if __name__ == "__main__":
    # 替换为你要遍历的实际文件夹路径
    # Windows路径（加r避免反斜杠转义）
    target_folder = r"D:\pythonProject\python_work\处理excel\BaselineLab_10.200.142.44_1778482407_8418111"
    result = dir_file_key(target_folder, "爱立信和中信科")
    print(result)
