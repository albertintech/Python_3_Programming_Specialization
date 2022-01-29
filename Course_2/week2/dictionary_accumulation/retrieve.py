"""Obtain text from an exercise"""

fileref = open("text_name_here.txt", "r")
contents = fileref.read()
print(contents)
fileref.close()
