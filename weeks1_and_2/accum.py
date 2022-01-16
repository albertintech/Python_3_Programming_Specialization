nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)  # print to console: 55

accum = 0
for w in range(11):
    accum = accum + w
print(accum)  # print to console: 55

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums:
    accum = 0
    accum = accum + w
print(accum)
