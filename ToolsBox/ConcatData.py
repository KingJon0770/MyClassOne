import polars as pl
import pandas as pd
"""
支持传入 0~N 个表
自动跳过空表，不会报错
统一返回 Pandas DataFrame
无数据时返回空 Pandas 表
适合数据 pipeline、ETL、报表合并等场景
"""
def concat_data(*args: pl.DataFrame) -> pd.DataFrame:
    """
    垂直拼接任意数量的 Polars DataFrame,自动过滤空表,返回 Pandas DataFrame
    """
    # 过滤非空 DataFrame
    valid_dfs = [df for df in args if not df.is_empty()]
    
    # 拼接 + 转 Pandas
    if valid_dfs:
        concat_df = pl.concat(valid_dfs, how="vertical")
    else:
        concat_df = pl.DataFrame()  # 空表
    
    return concat_df.to_pandas()

if __name__=="__main__":
        # 构造测试数据
    df1 = pl.DataFrame({"a": [1,2]})
    df2 = pl.DataFrame()  # 空表
    df3 = pl.DataFrame({"a": [3,4]})
    df4=None
    # 调用函数
    result = concat_data(df1, df2, df3)

    print(type(result))  # <class 'pandas.core.frame.DataFrame'>
    print(result)
    # 输出
    #    a
    # 0  1
    # 1  2
    # 2  3
    # 3  4