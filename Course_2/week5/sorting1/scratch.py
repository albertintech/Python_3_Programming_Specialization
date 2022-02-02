"""Sorting Basics"""
# l1 = [1, 7, 4, -2, 3]
# l2 = ["Cherry", "Apple", "Blueberry"]

# l1.sort()
# print(l1)
# l2.sort()
# print(l2)

l2 = ["Cherry", "Apple", "Blueberry"]
print("Original: ", l2)
print("Has object id: ", id(l2))
# sorted() creates a copy of original list and returns a new object
l3 = sorted(l2)
print("New object created by sort method: ", l3)
print("Has object id: ", id(l3))
print("Original: ", l2)
print("Has object id: ", id(l2))

print(sorted("Apple"))  # returns a list of chars in alpha order
"Apple".sort()  # will fail, only works on list
