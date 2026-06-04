s="programming"
duplicate=[]
for ch in s:
    if s.count(ch) > 1 and ch not in duplicate:
        duplicate.append(ch)
print(duplicate)