string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
str2 = string1.lower()

letter_counts = {}

for c in str2:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1
print(letter_counts)
