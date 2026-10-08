numbers = [3, -2, 5, -7, 0, 8, -1, 0, 4]
positive=0
negative=0
zero=0
for i in numbers:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+=1
print(positive,negative,zero)