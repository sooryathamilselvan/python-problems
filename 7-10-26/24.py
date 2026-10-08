numbers = [12, 5, 28, 7, 19, 3]
largest=numbers[0]
largest_index=0
for i in range(len(numbers)):
    if numbers[i]>largest:
        largest=numbers[i]
        largest_index=i
print(largest_index)