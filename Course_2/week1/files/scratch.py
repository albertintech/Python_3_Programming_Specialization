
# fileref = open("olympics.txt", "r")
# lines = fileref.readlines()
# print(lines)
# for line in lines[:4]:
#     print(line.strip())
# fileref.close()

# # the Pythonic Way of iterating over each line in the file
# # However, slicing is not supported; use readlines if slicing is required
# fileref = open("olympics.txt", "r")
# # lines = fileref.readlines()
# for line in fileref:
#     print(line.strip())
# fileref.close()

file_obj = open("squares.txt", "w")
for number in range(13):
    square = number * number
    file_obj.write(str(square) + '\n')
    # file_obj.write('\n')
file_obj.close()

new_file_obj = open("squares.txt", "r")
print(new_file_obj.read())
