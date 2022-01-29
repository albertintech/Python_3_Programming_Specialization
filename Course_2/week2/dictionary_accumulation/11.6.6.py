f = open('scarlet.txt', 'r')
txt = f.read()

letter_counts = {}

for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")
print("' ': " + str(letter_counts[' ']) + " occurrences")
