# 创建一个购物清单程序，用列表记录商品，字典记录价格。
goods = ["apple","banana","orange"]
prices = {"apple":5,"banana":3,"orange":4}

print("购物清单:")

for item in goods:
    print("- ", item, ": ", "￥", prices[item])

print("总价: ", sum(prices.values()), "元")

# 点号"."获取字典的所有keys
for item in prices.keys():
    print(item)
