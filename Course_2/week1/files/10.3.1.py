"""Using the file school_prompt.txt, find the number of characters in the file and assign that value to the variable num_char."""


fileref = open("school_prompt.txt", "r")
contents = fileref.read()
num_char = len(contents)
print(num_char)
fileref.close()
