from re import sub


def sublist(lst):
    sublst = []
    n = 0
    while n < len(lst):
        if lst[n] == "STOP":
            break
        else:
            sublst.append(lst[n])
        n += 1
    return sublst


words = ["go", "add", "divide", "continue", "STOP"]
a = sublist(words)
print(a)
