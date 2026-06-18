import pandas as pd
import os

def convert_data_to_py(file_path, py_file_path=None, var_name="data"):
    """
    将CSV/XLSX文件转换为.py文件(数据以列表+字典形式存储)
    
    参数说明：
    file_path: 输入的CSV/XLSX文件路径(如 "data.csv" 或 "data.xlsx")
    py_file_path: 输出的.py文件路径,默认和原文件同目录、同名(如 data.csv → data.py)
    var_name: 存储数据的Python变量名,默认是 "data"
    """
    # 处理默认输出路径
    if py_file_path is None:
        file_dir, file_name = os.path.split(file_path)
        file_name_no_ext = os.path.splitext(file_name)[0]
        py_file_path = os.path.join(file_dir, f"{file_name_no_ext}.py")
    
    # 读取数据(自动识别CSV/XLSX)
    try:
        if file_path.endswith(".csv"):
            # 读取CSV,自动处理编码(优先utf-8,失败则用gbk)
            try:
                df = pd.read_csv(file_path, encoding="utf-8")
            except:
                df = pd.read_csv(file_path, encoding="gbk")
        elif file_path.endswith(".xlsx"):
            # 读取XLSX
            df = pd.read_excel(file_path, engine="openpyxl")
        else:
            raise ValueError("仅支持.csv和.xlsx格式!")
    except Exception as e:
        print(f"读取文件失败：{e}")
        return False
    
    # 将DataFrame转换为列表+字典格式(每行是一个字典,键为列名)
    data = df.fillna("").to_dict("records")  # 空值填充为空字符串,避免报错
    
    # 写入.py文件
    try:
        with open(py_file_path, "w", encoding="utf-8") as f:
            # 写入注释+变量定义
            f.write(f"# 由 {os.path.basename(file_path)} 转换而来\n")
            f.write(f"# 数据格式：列表包含字典,每个字典对应一行数据(键=列名,值=单元格值)\n")
            f.write(f"{var_name} = {repr(data)}\n")  # repr确保特殊字符正确转义
        print(f"转换成功！输出文件：{py_file_path}")
        return True
    except Exception as e:
        print(f"写入.py文件失败:{e}")
        return False

# ------------------- 示例使用 -------------------
if __name__ == "__main__":
    # 替换为你的CSV/XLSX文件路径
    input_file = r"D:\pythonProject\python_work _polars\处理数据dataToPy\5G节能情况20260316085304.csv"  # 也可以是 "test_data.xlsx"
    # 执行转换(输出的.py文件默认和输入文件同目录、同名)
    input_file2=r"D:\pythonProject\python_work _polars\处理数据dataToPy\参数留痕参照表.xlsx"
    # convert_data_to_py(input_file,py_file_path='节能现状.py')
    convert_data_to_py(input_file2,py_file_path='参数留痕参照表.py')
