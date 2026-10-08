numbers = [1, 2, 3, 5, 6]
for i in range(1,len(numbers)+1):
    if i not in numbers:
        print(numbers[i])
        break