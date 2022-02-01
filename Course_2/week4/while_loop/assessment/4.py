def stop_at_z(lst):
    sublst = []
    n = 0
    while n < len(lst):
        if lst[n] == "z":
            break
        else:
            sublst.append(lst[n])
        n += 1
    return sublst


words = ["go", "add", "div", "quark", "z"]
a = stop_at_z(words)
print(a)
