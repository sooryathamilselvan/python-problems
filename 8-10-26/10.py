numbers = [10, 5, 8, 20, 15, 30, 25]
ound=False
sum=0
for i in range(len(numbers)):
    if numbers[i]==20:
        ound=True
    elif ound:
        sum+=numbers[i]
print(sum)