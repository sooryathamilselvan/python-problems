n = [1, 2, 3, 4, 5, 5, 3, 2]
m = [2, 4, 5]
freq_map = {}
for i in n :
    if i in freq_map:
        freq_map[i]+=1
    else:
        freq_map[i]=1
count=0
for x in m:
    if x in freq_map:
        count+=1
print (count)