def createFile(filename):
    with open(filename, 'w') as f:
        f.write("")

def writeFile(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')

def readFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines

fileExample = createFile('example.txt')
writeFile('example.txt', 'Hello, world!')
print(readFile('example.txt'))  

# AI生成的代码
def write_diary():
    content = input("请输入今天的日记：")
    with open("diary.txt", "a") as f:
        f.write(content + "\n")
    print("日记已保存！")

def read_diary():
    try:
        with open("diary.txt", "r") as f:
            print("\n=== 日记内容 ===")
            print(f.read())
    except FileNotFoundError:
        print("还没有日记！")

# 使用示例
write_diary()
read_diary()