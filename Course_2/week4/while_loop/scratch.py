# Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
eve_nums = []
n = 0
while n <= 15:
    if n % 2 == 0:
        eve_nums.append(n)
    n += 1
print(eve_nums)

# Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.

list1 = [8, 3, 4, 5, 6, 7, 9]

# tot = 0
# for elem in list1:
#     tot = tot + elem

idx = 0
accum = 0
while idx < len(list1):
    accum = accum + list1[idx]
    print(accum)
    idx += 1
