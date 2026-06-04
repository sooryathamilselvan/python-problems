value=[1,2,3,0,5,0,6,0]
result =[]
for zeros in value:
    if zeros!=0:
        result.append(zeros)
zero_count=value.count(0)
for i in range(zero_count):
    result.append(i)



print (result)