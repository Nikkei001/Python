def Fibonacci(n):
    if n<0:
        print("Incorrect input");
    elif n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

fibonacciList = [Fibonacci(i) for i in range(20)];
print(fibonacciList);

# AI给出的代码
n = 20
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
print(f"前{n}项斐波那契数列：{fib}")