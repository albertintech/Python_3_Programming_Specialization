s1 = "hello"

counts = {}

for c in s1:
    if c not in counts:
        counts[c] = 0
    counts[c] += 1
print(counts)
