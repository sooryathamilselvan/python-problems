n=153
num = n 
total = 0
nod=len(str(n))
while num > 0:
    ld = num % 10
    total = (ld**nod)+total
    num = num // 10 
if total == n :
    print(True)
else:
    print(False)
    