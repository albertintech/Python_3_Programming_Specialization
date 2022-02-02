# lambda args: return_value

def f(x):
    return x - 1


print(f)
print(type(f))
print(f(3))

print(type(lambda x: x-2))
print((lambda x: x-2)(6))


def last_char(s):
    return[-1]


last_char = (lambda s: s[-1])
print(last_char("Batman"))
