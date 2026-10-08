numbers = [10, 5, 8, 20, 15, 30, 25]
found = False

for i in range(len(numbers)):
    if numbers[i] == 20:
        found = True
    elif found:
        print(numbers[i])
        break