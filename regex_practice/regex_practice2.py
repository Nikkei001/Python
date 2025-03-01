# 现在有一些产品sku,需要将sku中的产品编号提取出来,已知产品编号都是"I87"开头且长度为12位
# 这些产品编号存放在一个excel文件中,列名为"sku",请编写python代码提取产品编号.
import pandas as pd
import re

# 读取Excel文件
df = pd.read_excel('D:/Users/Administrator/Desktop/临时计算/产品编号提取.xlsx', sheet_name='Sheet1')

# 定义正则表达式模式
pattern = r'I87\w{7}'

# 提取符合条件的产品编号
df['产品编号'] = df['sku'].apply(lambda x: re.search(pattern, str(x)).group() if re.search(pattern, str(x)) else None)


# 保存结果到新的Excel文件
df.to_excel('extracted_product_numbers.xlsx', index=False)

print("提取完成,结果已保存到 'extracted_product_numbers.xlsx'")
