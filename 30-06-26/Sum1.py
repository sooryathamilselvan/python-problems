def count(x, n):
    if n == 0:
        return
    print(x)
    count(x, n - 1)

count(15, 4)