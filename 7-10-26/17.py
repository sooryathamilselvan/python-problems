numbers = [10, 5, 8, 20, 15, 3]
secondlargest=0
largest=numbers[0]
for i in numbers:
    if i>largest:
        secondlargest=largest
        largest=i
    elif i!=largest and i>secondlargest:
        secondlargest=i
print(secondlargest)