eng2sp = {}

eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

print(eng2sp)

# Alternatively:
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}

value = eng2sp['two']
print(value)
print(eng2sp['one'])

eng2rus = {}
eng2rus['one'] = 'adin'
eng2rus['two'] = 'dva'
eng2rus['three'] = 'trri'

print(eng2rus)

# It doesn’t matter what order we write the pairs. The values in a dictionary are accessed with keys, not with indices, so there is no need to care about ordering.

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['bananas'] += 200
print(inventory)
numItems = len(inventory)
print(numItems)

for key in inventory.keys():
    print(key, "has the value", inventory[key])

keys = list(inventory.keys())
print(keys)

for k in inventory:
    print("Got key", inventory[k])

print(list(inventory.values()))  # list of values
print(list(inventory.items()))  # list of tuples of each key-value pair

for k, v in inventory.items():
    print("Got", k, "that maps to", v)
