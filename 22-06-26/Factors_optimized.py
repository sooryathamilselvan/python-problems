from  math import sqrt 
num = 20
result = []
for i in range (1,int(sqrt(num))):
    if num % i == 0:
        result.append(i)
        if num//i!= i:
            result.append(num//i)
result.sort()
print(result)
