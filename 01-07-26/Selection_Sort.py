def selectionsort(num):
    n = len(num)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if num[min_index]>num[j]:
                j = min_index
        num[i],num[min_index]=num[min_index],num[i]
    return num
text = [1, 2, 5, 4, 7, 5]
print(selectionsort(text))