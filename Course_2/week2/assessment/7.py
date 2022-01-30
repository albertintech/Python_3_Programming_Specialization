sally = "sally sells sea shells by the sea shore and by the road"

characters = {}
worst_char = 0
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1
print(characters)
keys = list(characters.keys())
worst_char = keys[0]

for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char = key
print(worst_char)
