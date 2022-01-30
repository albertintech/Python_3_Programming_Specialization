str1 = "peter piper picked a peck of pickled peppers"

freq = {}

for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] += 1
print(freq)
