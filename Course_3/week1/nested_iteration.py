nested1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]

for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

info = [['Tina', 'Turner', 1939, 'singer'],
        ['Matt', 'Damon', 1970, 'actor'],
        ['Kristen', 'Wiig', 1973, 'comedian'],
        ['Michael', 'Phelps', 1985, 'swimmer'],
        ['Barack', 'Obama', 1961, 'president']]

# last_names = []
# for lst in info:
#     for x in lst:
#         if x == lst[1]:
#             last_names.append(x)
# print(last_names)

last_names = []
for lst in info:
    last_names.append(lst[1])
print(last_names)

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'],
     ['carrots', 'peas', 'cucumbers', 'green beans'],
     ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for lst in L:
    for item in lst:
        if 'b' in item:
            b_strings.append(item)
print(b_strings)
