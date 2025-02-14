import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = 'd:/Users/Administrator/Desktop/临时计算/折线图画图.xlsx'

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 读取 Excel 文件
df = pd.read_excel(file_path, sheet_name='Sheet1')

# 打印读取的数据（可选）
print(df)

# 按年月分组
grouped = df.groupby(df['YearAndMonth'])

# 打印分组结果（可选）
print(grouped)

# 定义颜色列表
colors = ['black', 'blue', 'red']

# 绘制折线图
plt.figure(figsize=(18, 6))
for i, (name, group) in enumerate(grouped):
    plt.plot(group['Date'], group['Orders'], label=name, color=colors[i % len(colors)])

# 设置x轴和y轴的标题大小
plt.xlabel('Date', fontsize=20)
plt.ylabel('Orders', fontsize=20)

# 设置刻度范围和间隔
plt.xticks(np.arange(1, 32, 1))

# 设置刻度大小
plt.tick_params(axis='both', which='major', labelsize=15, length=6, width=2, pad = 1)
plt.legend(title='YearAndMonth')
plt.grid(True)
# plt.show()

plt.savefig("d:/Users/Administrator/Desktop/折线图2.jpg")




