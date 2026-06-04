arr=[1,9,3,4,5,4,6,4]
largest=arr[0]
second_largest=arr[0]
for i in arr:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i !=largest:
        second_largest=i

print(second_largest)