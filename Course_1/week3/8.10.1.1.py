nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0  # This is hard coded to zero, which is not good
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]  # This is coded to the first index, which is good
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)
