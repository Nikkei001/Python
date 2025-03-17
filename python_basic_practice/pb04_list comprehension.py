# 列表推导式基本语法
# 列表推导式是一种简洁的方式来创建新的列表。它通常由方括号 [] 包围，内部包含一个表达式和一个或多个 for 循环。
# 基本语法如下：
# new_list = [expression for item in iterable if condition]
# new_list = [expression for item1 in iterable1 for item2 in iterable2 ... if condition]

# 创建一个包含 0 到 9 的列表
fromZeroToNine = [number for number in range(10)]
print(fromZeroToNine)

# 创建一个包含 0 到 9 的平方的列表
squareOfZeroToNine = [number**2 for number in range(10)]
print(squareOfZeroToNine)

# 创建一个包含 0 到 9 的偶数的列表 
evenNumbersOfZeroToNine = [number for number in range(10) if number % 2 == 0]
print(evenNumbersOfZeroToNine)

