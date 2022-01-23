fname = "yourfile.txt"

# loads file then iterates
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for line in lines:                     # step 3
        # some code that references the variable lin
        # some other code not relying on fileref   # step 4


with open(fname, 'r') as fileref:
    for lin in fileref:
        # some code that uses line as the current line of the file
        # some more code
