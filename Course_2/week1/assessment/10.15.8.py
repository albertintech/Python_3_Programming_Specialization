'''Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.'''

# fileref = open("school_prompt.txt", "r")
# three = []
# for line in fileref.readlines():
#     lst = line.split(',')
#     word_lst = lst.split(',')
#     # three.append(lst[2])
#     print(word_lst)
# fileref.close()

# fileref = open("school_prompt.txt", "r")
# # three = []
# for line in fileref.readlines():
#     lst = line.split(',')
#     print(lst[0], "is the first item")
# fileref.close()

sp_file = open("school_prompt.txt", "r")
three = []
for a_line in sp_file:
    values = a_line.split(",")
    strings = values[0]
    three.append(strings.split()[2])
three.pop()
three.append('ups,')
print(three)
sp_file.close()
