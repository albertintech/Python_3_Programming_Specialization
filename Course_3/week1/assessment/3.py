# Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'],
     [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = False
for word in L[1]:
    if word == 'hola':
        test1 = True
print(test1)

# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = False
if [5, 8, 7] in L:
    test2 = True
print(test2)
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = False
for lst in L:
    for item in lst:
        if item == 6.6:
            test3 = True
print(test3)
