def fibonacci(num):
    if num == 0 or num == 1:
        return num

    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b

    return b


num = int(input("Enter a number:"))
print(fibonacci(num))
