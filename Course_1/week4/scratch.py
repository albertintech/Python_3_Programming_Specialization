# alist = ['a', 'd', 'f']
# print(alist)
# alist[1:1] = ['b', 'c']
# print(alist)
# alist[4:4] = ['e']
# print(alist)

# phrase = "many moons"
# print(phrase)
# phrase_expanded = phrase + " and many stars"
# print(phrase_expanded)
# phrase_larger = phrase_expanded + " litter"
# print(phrase_larger)
# phrase_complete = "M" + phrase_larger[1:] + " the night sky."
# print(phrase_complete)
# excited_phrase_complete = phrase_complete[:-1] + "!"
# print(excited_phrase_complete)

# a = ['one', 'two', 'three']
# del a[1]
# print(a)

# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# del alist[1:5]
# print(alist)

# a = "banana"
# b = "banana"

# print(a is b)

# a = "banana"
# b = "banana"

# print(id(a))
# print(id(b))

# a = [81, 82, 83]
# b = [81, 82, 83]

# print(a is b)

# print(a == b)

# print(id(a))
# print(id(b))

# alist = [4, 2, 8, 6, 5]
# blist = alist * 2
# blist[3] = 999
# print(alist)

mylist = []
print(id(mylist))
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
mylist.append(99)
# print(mylist)

mylist.insert(1, 12)
# print(mylist)

print(mylist.count(12))  # counts the occurances of 12 => 2

# Returns the index of the first position of argument
print("What is the index of 99? Answer:", mylist.index(99))
print(mylist.count(5))
print(id(mylist))

# mylist.reverse()
# print(mylist)

# mylist.sort()
# print(mylist)

# mylist.remove(5)
# print(mylist)

# lastitem = mylist.pop()
# print(lastitem)
# print(mylist)
