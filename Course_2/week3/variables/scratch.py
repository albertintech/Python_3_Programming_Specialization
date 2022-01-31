# def addit(i):
#     i += 5
#     return i


# def mult(j):
#     k = j * addit(j)
#     return k


# print(mult(1))

def accum(lst):
    tot = 0
    for i in range(0, len(lst)):
        tot += lst[i]
    return tot


int_lst = [2, 3]
tot = accum(int_lst)
print(tot)
