numbers = [4, 7, 2, 9, 7, 5, 2]
seen = []

for i in numbers:
    if i in seen:
        print(i)
        break
    else:
        seen.append(i)