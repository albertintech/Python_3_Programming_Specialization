"""Create a dictionary called d that keeps track of all the characters in the string quote and notes how many times each character was seen. Then find the key with the lowest value in this dictionary and assign that key to min_value."""

quote = "Happy families are all alike; every unhappy family is unhappy in its own way."

d = {}

for c in quote:
    if c not in d:
        d[c] = 0
    d[c] = d[c] + 1
print(d)

keys = list(d.keys())
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key

print(min_value)
