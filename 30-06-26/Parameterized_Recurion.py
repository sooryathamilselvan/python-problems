def recursion(sum,i,n):
    if i>n:
        print(sum)
        return
    recursion(sum+i,i+1,n)
recursion(0,1,4)
