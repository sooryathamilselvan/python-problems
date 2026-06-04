arr1 =[1,2,3,3,4,5,]
arr2=[2, 4,6]
common = []
for char in arr1:
    if char in arr2 and char not in common:
        common.append(char)
print(common)