def check_nums(lst):
    sublst = []
    n = 0
    while n < len(lst):
        if lst[n] == 7:
            break
        else:
            sublst.append(lst[n])
        n += 1
    return sublst


list1 = [8, 3, 4, 5, 6, 7, 9]
a = check_nums(list1)
print(a)
