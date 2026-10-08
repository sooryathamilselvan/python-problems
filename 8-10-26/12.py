numbers = [10, 5, 8, 20, 15, 30, 25, 12, 40]
largest=numbers[0]
found=False
for i in range(len(numbers)):
    if numbers[i]==20:
        found=True
    elif found and numbers[i]>largest:
        largest=numbers[i]
print(largest)
