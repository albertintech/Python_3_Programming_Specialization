p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p_low = p.lower()

low_d = {}
for c in p_low:
    if c not in low_d:
        low_d[c] = 0
    low_d[c] += 1
print(low_d)
