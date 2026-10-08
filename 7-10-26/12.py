numbers = [3, 8, 2, 15, 6, 7, 10, 11]
even=0
odd=0
for i in numbers:
    if i %2 ==0:
        even+=1
    else:
        odd+=1
print(even,odd)