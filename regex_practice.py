import pandas as pd
import re
# 指定 Excel 文件路径
file_path = 'd:/Users/Administrator/Desktop/临时计算/20250113产品零件问题次数统计/12月客诉整理_副本.xlsx'  # 替换为你的 Excel 文件路径
# 读取 Excel 文件
df = pd.read_excel(file_path, sheet_name='原始数据')
# 打印读取的数据（可选）
print(df)

# 定义一个函数来删除"X个"这样的文本
def remove_quantity(text):
    return re.sub(r'\d+个', '', str(text))

# 定义一个函数来将英文字母转换为大写
def convert_to_uppercase(text):
    # 使用正则表达式匹配英文字母，并将其转换为大写
    return re.sub(r'[a-zA-Z]+', lambda x: x.group(0).upper(), str(text))

# 正则表达式匹配规则
def extract_complex(text):
    patterns = [
        r'\bLED\b',  # 单独匹配 LED
        r'\b[a-zA-Z]\b',  # 单个英文字母（除了已匹配的 LED）
        r'\b[a-zA-Z]{2,}\b',  # 多个英文字母（除了已匹配的 LED）
        r'\d+',  # 单个数字
        r'[a-zA-Z0-9]+',  # 字母和数字的组合
        r'五金包|遥控器|镜子'  # 特定词语
    ]
    
    results = []
    for pattern in patterns:
        matches = re.findall(pattern, str(text))
        results.extend(matches)
    
    # 去重并用逗号连接
    return ','.join(sorted(set(results)))

# 应用函数到"问题说明"列
df['提取零件编号'] = df['问题说明'].apply(remove_quantity).apply(convert_to_uppercase)
df['提取零件编号'] = df['提取零件编号'].apply(extract_complex)

# 拆分行的函数

def split_rows(df, column_to_split='提取零件编号', separator=','):
    # 确保要拆分的列存在
    if column_to_split not in df.columns:
        raise ValueError(f"列 '{column_to_split}' 不在DataFrame中")

    # 创建一个新的DataFrame来存储拆分后的结果
    new_rows = []

    for index, row in df.iterrows():
        # 获取要拆分的值
        values_to_split = row[column_to_split].split(separator)
        
        # 为每个拆分的值创建一个新行
        for value in values_to_split:
            new_row = row.copy()
            new_row[column_to_split] = value.strip()  # 去除可能的空白
            new_rows.append(new_row)

    # 创建新的DataFrame
    return pd.DataFrame(new_rows).reset_index(drop=True)

# 使用示例
# 假设 df 是您的原始DataFrame
split_df = split_rows(df)

# 汇总结果
summary_results = split_df[split_df['提取零件编号'].notna() & (split_df['提取零件编号'] != '')].groupby(['产品编号', '提取零件编号']).size().reset_index(name='出现次数')
summary_results = summary_results.sort_values('出现次数', ascending=False).reset_index(drop=True)

with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
# 将更新后的数据保存到 Excel 文件中
    split_df.to_excel(writer, sheet_name='原始数据', index=False)
    summary_results.to_excel(writer, sheet_name='汇总结果', index=False)







