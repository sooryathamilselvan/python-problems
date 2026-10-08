numbers = [15, 8, 23, 4, 19, 7]
smallest = numbers[0]
smallest_index = 0
for i in range(len(numbers)):
    if numbers[i] < smallest:
        smallest=numbers[i]
    smallest_index=i
print(smallest_index)