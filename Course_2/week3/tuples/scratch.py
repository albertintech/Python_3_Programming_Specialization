a = 1
b = 2
print(a, b)
temp = a
a = b
b = temp
print(a, b, temp)

a = 4
b = 5
(a, b) = (b, a)
print(a, b)

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

print()

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])

print()

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012),
              ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []
for t in tuples_lst:
    country.append(t[1])

print(country)
