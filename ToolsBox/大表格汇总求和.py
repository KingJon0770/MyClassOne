import os
import pandas as pd


def aggregate_prb_data(folder_path):
    """
    汇总文件夹中所有Excel文件的PRB数据，并将结果保存到该文件夹下的"PRB汇总.xlsx"

    Args:
        folder_path: Excel文件所在文件夹路径

    Returns:
        汇总后的DataFrame，若失败则返回None
    """
    # 定义输出文件路径（保存在目标文件夹下）
    output_file = os.path.join(folder_path, "PRB汇总.xlsx")

    # 存储所有读取的数据
    all_data = []

    # 获取文件夹中所有Excel文件（排除临时文件和汇总结果文件）
    excel_extensions = ('.xlsx', '.xls')
    excel_files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(excel_extensions)
           and not f.startswith('~$')
           and f != "PRB汇总.xlsx"  # 排除已生成的汇总文件
    ]

    if not excel_files:
        print("⚠️ 错误：指定文件夹中未找到任何待处理的Excel文件！")
        return None

    # 定义需要处理的列
    target_columns = ['基站ID', '小区ID', '下行实际平均占用PRB资源个数', '下行可用的PRB个数']

    # 读取并验证每个Excel文件
    for file_name in excel_files:
        file_path = os.path.join(folder_path, file_name)
        print(f"📄 正在处理文件: {file_name}")

        try:
            # 读取Excel文件，只加载需要的列
            df = pd.read_excel(file_path, usecols=target_columns)

            # 检查必要列是否存在
            missing_cols = [col for col in target_columns if col not in df.columns]
            if missing_cols:
                print(f"❌ 文件 {file_name} 缺少列：{missing_cols}，已跳过")
                continue

            # 数据清洗：空值填充为0，确保数值类型正确
            df = df.fillna({
                '下行实际平均占用PRB资源个数': 0,
                '下行可用的PRB个数': 0
            })
            df['下行实际平均占用PRB资源个数'] = pd.to_numeric(df['下行实际平均占用PRB资源个数'],
                                                              errors='coerce').fillna(0)
            df['下行可用的PRB个数'] = pd.to_numeric(df['下行可用的PRB个数'], errors='coerce').fillna(0)

            all_data.append(df)

        except Exception as e:
            print(f"❌ 处理文件 {file_name} 失败: {str(e)}")
            continue

    if not all_data:
        print("⚠️ 错误：没有成功读取任何有效数据！")
        return None

    # 合并所有数据并分组求和
    combined_df = pd.concat(all_data, ignore_index=True)
    aggregated_df = combined_df.groupby(
        ['基站ID', '小区ID'],
        as_index=False
    ).agg({
        '下行实际平均占用PRB资源个数': 'sum',
        '下行可用的PRB个数': 'sum'
    })

    # 重命名列名（添加合计标识）
    aggregated_df.rename(columns={
        '下行实际平均占用PRB资源个数': '下行实际平均占用PRB资源个数_合计',
        '下行可用的PRB个数': '下行可用的PRB个数_合计'
    }, inplace=True)

    # 保存汇总结果到指定文件夹
    try:
        aggregated_df.to_excel(output_file, index=False, engine='openpyxl')
        print("\n✅ 汇总完成！")
        print(f"📊 共处理 {len(excel_files)} 个Excel文件")
        print(f"📈 汇总得到 {len(aggregated_df)} 个唯一的基站+小区组合")
        print(f"💾 结果文件路径：{output_file}")

        # 显示前5行结果预览
        print("\n📋 汇总结果预览：")
        print(aggregated_df.head())

    except Exception as e:
        print(f"❌ 保存文件失败: {str(e)}")
        return None

    return aggregated_df


# 主程序入口
if __name__ == "__main__":
    # ======================
    # 请修改为你的文件夹路径
    # ======================
    # 示例路径（Windows）：r"C:\Users\XXX\Documents\基站数据"
    # 示例路径（Mac/Linux）："/Users/XXX/Documents/基站数据"
    FOLDER_PATH = r"C:\Users\15828\Desktop\py\练习3"

    # 检查文件夹是否存在
    if not os.path.exists(FOLDER_PATH):
        print(f"❌ 错误：文件夹 {FOLDER_PATH} 不存在！")
    else:
        # 执行汇总
        aggregate_prb_data(FOLDER_PATH)