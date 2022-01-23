
fileref = open("olympics.txt", "r")
lines = fileref.readlines()
for line in lines[:4]:
    print(line.strip())
fileref.close()

# the Pythonic Way of iterating over each line in the file
# However, slicing is not supported; use readlines if slicing is required
fileref = open("olympics.txt", "r")
# lines = fileref.readlines()
for line in fileref:
    print(line.strip())
fileref.close()
