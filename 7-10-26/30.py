numbers = [12, 5, 28, 7, 19, 3]
smallest=numbers[0]
largest=numbers[0]
diff=0
for i in range(len(numbers)):
    if smallest>numbers[i]:
        smallest=numbers[i]
    if largest<numbers[i]:
        largest=numbers[i]
diff = largest-smallest
print(diff)