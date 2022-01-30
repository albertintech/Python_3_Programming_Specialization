Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3,
          'TO 313': 3, 'BCOM 350': 1, 'MO 300': 3}

credits = 0
for course in Junior:
    credits += Junior[course]
print(credits)
