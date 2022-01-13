"""It is also possible to perform list traversal using iteration by item. A list is a sequence of items, so the for loop iterates over each item in the list automatically."""

fruits = ["apple", "orange", "banana", "cherry"]

"""It almost reads like natural language: For (every) fruit in (the list of) fruits, print (the name of the) fruit."""

for afruit in fruits:
    print(afruit)

print("This will execute first")

for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside of the for loop!")
"""
_ is a strange name for a variable but if you look carefully at the rules about variable names, it is a legal name. By convention, we use the _ as our loop variable when we don’t intend to ever refer to the loop variable. That is, we are just trying to repeat the code block some number of times (once for each item in a sequence), but we are not going to do anything with the particular items. _ will be bound to a different item each time, but we won’t ever refer to those particular items in the code.
"""
