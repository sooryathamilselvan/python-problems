numbers = [3, 8, 2, 15, 6, 7, 10]
count=0
total=0
for i in numbers:
    if i %2 ==0:
        total+=1
        count+=1
print(count,total)