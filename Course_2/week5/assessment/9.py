# Create a function called last_four that takes in a single ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use the resulting function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.

def last_four(x):
    lst_x = []
    lst_x = list(str(x))
    last_four = lst_x[-4:]
    acc = ''
    for i in last_four:
        acc += i
    return int(acc)


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# short = []

# for n in ids:
#     short.append(last_four(n))

# sorted_ids = sorted(short)
# print(sorted_ids)

sorted_ids = sorted(ids)
print(sorted_ids)
