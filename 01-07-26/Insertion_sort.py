nums = [3, 5, 1, 7, 9, 2, 4]
n = len(nums)

for i in range(1, n):
    key = nums[i]
    j = i - 1          # Initialize j

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

print(nums)