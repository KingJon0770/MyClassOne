import chardet
import pandas as pd


def detect_encoding(csv_file_path):
    with open(csv_file_path, 'rb') as f:
        try:
            result_encoding = chardet.detect(f.readline()).get('encoding', 'gbk')
            if result_encoding != 'utf-8':
                return 'gbk'
        except UnicodeEncodeError as e:
            return 'utf-8'
    # encoding_errors='ignore' 忽略编码错误
    if not f:
        raise FileNotFoundError("File could not be opened.")

    return result_encoding


def read_csv_file(file_path):
    csv_df = pd.read_csv(file_path, encoding=detect_encoding(file_path))
    # print(csv_df)
    return csv_df


def csv_replace_tab(csv_file):
    # 调用解码方式
    df_check = read_csv_file(csv_file)
    # 处理标题行（列名）中的制表符
    new_columns = []
    for col in df_check.columns:
        # 移除制表符和多余空格
        cleaned_col = col.replace('\t', '').strip()
        # 移除引号（如果存在）
        # cleaned_col = cleaned_col.replace('"', '')
        new_columns.append(cleaned_col)
    df_check.columns = new_columns
    # 处理数据单元格中的制表符
    for col in df_check.columns:
        if df_check[col].dtype == 'object':
            # 替换制表符为空格，同时保留原有文本结构
            df_check[col] = df_check[col].str.replace('\t', '', regex=False)
    return df_check


if __name__ == '__main__':
    file_check = r"D:\参数生产流程参数模板\呈阅：中兴区域5G上网特性参数核查\BaselineLab_10.200.136.37_1754564183_3563193\CheckResult_200_中移_上网特性参数检查_5G_700M-2.6G-4.9G_20250807185625.csv"

    print(read_csv_file(file_check).head(2))
    print(csv_replace_tab(file_check).head(2))
