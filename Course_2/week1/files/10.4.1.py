oly_file = open("olympics.txt", "r")

for line in oly_file.readlines():
    values = line.split(",")
    print(values[0], "is from", values[3],
          "and is on the roster for", values[4])

oly_file.close()
