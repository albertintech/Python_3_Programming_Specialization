phrase = "What a wonderful day to program"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot + 1
print("Total characters in phrase is:", len(phrase))
print("After whitespaces are removed, letters alone are:", tot)
