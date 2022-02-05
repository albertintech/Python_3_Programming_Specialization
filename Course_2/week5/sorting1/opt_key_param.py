"""Optional Key Parameter
From docs.python.org -> sorted function
sorted(iterable, /, *, key=None, reverse=False)
key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).
"""

L1 = ["x", "z", "y", "2", "a", "7", "P", "B"]

print(sorted(L1))
print(sorted(L1, key=str.lower))

L2 = [1, -7, 4, -2, 3, 8, -5]


def absolute(x):
    if x >= 0:
        return x
    else:
        return -x


print(sorted(L2))
print(sorted(L2, key=absolute))
