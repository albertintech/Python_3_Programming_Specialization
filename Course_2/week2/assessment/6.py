sally = "sally sells sea shells by the sea shore"

characters = {}
best_char = 0
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1

keys = list(characters.keys())
best_char = keys[0]

for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key
print(best_char)
