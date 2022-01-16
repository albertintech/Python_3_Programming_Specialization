sentence = "what if we went to the zoo"
vowels = ['a', 'e', 'i', 'o', 'u']
x = 0
for vowel in sentence:
    if vowel in vowels:
        x += 1
print("The given string has this number of vowel letters:", x)
