import os

def FormKey(file_dir, key=None):
    try:
        # 遍历目录
        for filename in os.listdir(file_dir):
            # 匹配文件类型
            if filename.endswith((".xlsx", ".csv")):
                # 不区分大小写查找关键词
                if key and key.upper() in filename.upper(): 
                    # 找到第一个就直接返回完整路径
                    return os.path.join(file_dir, filename)
        # 遍历完都没找到 → 返回 None
        return None
    
    except FileNotFoundError:
        # 目录不存在时返回 None
        return None

if __name__ == '__main__':
    file_dir = r"D:\pythonProject\pythonProject"
    result = FormKey(file_dir, "新建")
    print("\n最终返回:", result)