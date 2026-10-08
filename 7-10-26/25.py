numbers = [15, 8, 23, 4, 19, 7]

smallest = numbers[0]
second_smallest = numbers[0]

for i in numbers:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i > second_smallest and i != smallest:
        second_smallest = i

print(second_smallest)