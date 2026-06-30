#print 1 to n using recursion.
def count(i,n):
    if i>n:
        return
    
    count(i+1,n)
    print(i)
count(1,5)