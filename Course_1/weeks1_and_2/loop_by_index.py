fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(5):  # hard-coded value
    print(n, fruits[n])
print()

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):  # len function returns 5 as bound on range
    print(n, fruits[n])
print()

# the most pythonic way to code a simple loop
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for fruit in fruits:
    print(fruit)
print()

# the pythonic way to loop by index involves the enumerate function
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
print()

s = "python"
for idx in range(len(s)):
    print(s[idx % 2])
