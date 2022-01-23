fname = open('olympics.txt', 'r')
lines = fname.readlines()
header = lines[0]
h_names = header.strip().split(',')
print(h_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}: {}".format(vals[0], vals[4], vals[5]))
