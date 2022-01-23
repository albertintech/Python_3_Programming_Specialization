"""Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars."""

fileref = open("travel_plans.txt", "r")
contents = fileref.read()
first_chars = contents[:33]
# print(contents)
print(first_chars)
fileref.close()
