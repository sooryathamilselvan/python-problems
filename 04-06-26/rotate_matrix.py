martix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
n= len(martix)
rotated = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        rotated[j][n-1-i]=martix[i][j]
for row in rotated :
    print (row)