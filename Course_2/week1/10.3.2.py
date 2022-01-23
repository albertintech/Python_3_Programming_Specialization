"""Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines."""

fileref = open("travel_plans2.txt", "r")
lines = fileref.readlines()
num_lines = len(lines)
print(num_lines)
print(lines)
fileref.close()
