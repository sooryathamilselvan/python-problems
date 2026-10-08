numbers = [4, 7, 2, 9, 7, 5, 2]
seen=[]
for i in range(len(numbers)):
    if numbers[i] in seen:
        print(i)
        break
    else:
        seen.append(numbers[i])