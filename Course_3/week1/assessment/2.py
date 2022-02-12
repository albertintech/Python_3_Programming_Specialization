# Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10],
       ['green', 'yellow', 'purple', 'red']]

# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = False
for color in lst[2]:
    if color == 'yellow':
        yellow = True
print(yellow)

# Test to see if 4 is in the second list of lst. Save to variable ``four``
four = False
for item in lst[1]:
    if item == 4:
        four = True
print(four)

# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = False
for fruit in lst[0]:
    if fruit == 'orange':
        orange = True
print(orange)
