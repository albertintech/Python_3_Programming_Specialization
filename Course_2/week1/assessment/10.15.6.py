"""Assign to the variable num_lines the number of lines in the file school_prompt.txt."""

fileref = open("school_prompt.txt", "r")
lines = fileref.readlines()
num_lines = len(lines)
fileref.close()
