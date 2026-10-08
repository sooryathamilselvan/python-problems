numbers = [10, 5, 8, 20, 15, 3]
largest=numbers[0]
index=0
second_largest=numbers[0]
for i in range(0,len(numbers)):
    if numbers[i]>largest:
        second_largest = largest
        largest = numbers[i]
        index=i
    if numbers[i]>second_largest and numbers[i]!=largest:
        second_largest=numbers[i]
        index=i
print(index)