# Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]


def last_four(x):
    lst_x = []
    lst_x = list(str(x))
    last_four = lst_x[-4:]
    acc = ''
    for i in last_four:
        acc += i
    return int(acc)


sorted_id = sorted(ids, key=lambda num: last_four(num))
print(sorted_id)
