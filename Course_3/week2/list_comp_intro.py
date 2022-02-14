"""List Comprehensions"""

# Perform a math operation with list comprehension

things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)


def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list


num_lst = [3, 4, 6, 7, 0, 1]
print(keep_evens(num_lst))
