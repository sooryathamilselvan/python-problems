numbers = [10, 20, 30, 40, 50]
avg=0
sum =0
count=0
total=0
for i in numbers:
    sum+=i
    count+=1
avg=sum/count
for i in numbers:
    if i >avg:
        total+=1
print(total)