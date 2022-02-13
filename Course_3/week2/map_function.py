things = [2, 5, 9]

# things4 = map((lambda value: 4*value), things)
# print(list(things4))

# # or all on one line
# print(list(map((lambda value: 5*value), [1, 2, 3])))


things4 = map((lambda value: 4*value), things)
print("We must specify the type of return output, or get: ", things4)
print("Pass the map return value to list before printing: ", list(things4))

print(list(map((lambda value: 5*value), [1, 2, 3])))
