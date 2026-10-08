numbers = [10, 5, 8, 20, 15, 30, 25]
num =0
for i in range(-1,len(numbers)-1,-1):
    if numbers[i]==20:
        break
    if numbers[i]!=20:
        num+=1
print(num)