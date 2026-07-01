def Selction(num):
    n=len(num)
    for i in range(n):
        max=i
        for j in range(i+1,n):
            if num[j]>num[max]:
                max=j
        num[i],num[max]=num[max],num[i]
    return num
text = [1, 2, 5, 4, 7, 5]
print(Selction(text))


