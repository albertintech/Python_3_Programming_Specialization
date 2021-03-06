L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

# iterate through range of length of L1: 0, 1, 2
# for i in range(len(L1)):
#     # print(i)
#     L3.append(L1[i] + L2[i])

# print(L3)

# for i in range(5):
#     print(i)

L4 = list(zip(L1, L2))
print(L4)

for (x1, x2) in L4:
    L3.append(x1+x2)
print(L3)

# using list comprehension
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)
