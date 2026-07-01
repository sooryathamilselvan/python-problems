def Fibonacci(num):
    if num == 0 or num == 1:
        return num
    return Fibonacci(num - 1) + Fibonacci(num - 2)
num = int(input())
total = 0
for i in range(num+1):
    total += Fibonacci(i)
print(total)