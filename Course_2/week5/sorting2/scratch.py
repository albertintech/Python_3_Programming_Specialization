"""Sorting Dictionaries, Breaking Ties"""
# Previously, you have used a dictionary to accumulate counts, such as the frequencies of letters or words in a text. For example, the following code counts the frequencies of different numbers in the list.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

print("Print without sorted fuction call:")
for x in d.keys():
    print("{} appears {} times".format(x, d[x]))

print("Call sorted function and assign result to new variable:")
y = sorted(d.keys())
for k in y:
    print("{} appears {} times".format(k, d[k]))

print("Sort by value with a lambda function:")
y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))

print("Use 'd' as first param is equal to previous")
# Equivalent to above, note first parameter is simply 'd'
y = sorted(d, key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))
