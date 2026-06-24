n = [1, 2, 3, 4, 5, 5, 3, 2]
m = [-2, 44, 5]

hash_map = [0] * 11

for i in n:
    hash_map[i] += 1
total = 0
for x in m:
    if 0 <= x <= 10:
        total += hash_map[x]

print(total)