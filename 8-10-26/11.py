numbers = [10, 5, 8, 20, 15, 30, 25, 12, 40]
found=False
count=0
for i in range(len(numbers)):
    if numbers[i]==20:
        found=True
    elif found:
        if numbers[i]>20:
            count+=1
print(count)