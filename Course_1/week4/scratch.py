alist = ['a', 'd', 'f']
print(alist)
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

phrase = "many moons"
print(phrase)
phrase_expanded = phrase + " and many stars"
print(phrase_expanded)
phrase_larger = phrase_expanded + " litter"
print(phrase_larger)
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
print(phrase_complete)
excited_phrase_complete = phrase_complete[:-1] + "!"
print(excited_phrase_complete)
