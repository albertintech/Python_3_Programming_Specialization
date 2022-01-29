f = open('scarlet.txt', 'r')
txt = f.read()

letter_counts = {}

for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1

# print("t: " + str(letter_counts['t']) + " occurrences")
# print("e: " + str(letter_counts['s']) + " occurrences")
# print("' ': " + str(letter_counts[' ']) + " occurrences")

# A Clever Alternative:
# Replace the above for loop with these two lines:
# for c in txt:
#    letter_counts[c] = letter_counts.get(c, 0) + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")
