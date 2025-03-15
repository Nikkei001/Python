import random
randomNumber = random.randint(1,10)
inputNumber = 0
print(randomNumber)

while inputNumber != randomNumber:
    try:
        # 注意input总是返回字符串类型, 如果此处输入小数,由于int()不接受表示小数的字符串, 所以会报错
        inputNumber = int(input("请输入一个1到10的整数："))
    except:
        print("输入错误，请重新输入！")
        continue
    else:
        if inputNumber < randomNumber:
            print("你猜的数字太小了！")
            
        elif inputNumber > randomNumber:
            print("你猜的数字太大了！")

print("恭喜你，猜对了！")