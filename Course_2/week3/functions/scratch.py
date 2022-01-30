# def hello():
#     print("Hello")
#     print("Nice to meet you")
#     print()


# def hello2(s):
#     print("Hello " + s)
#     print("Nice to meet you")
#     print()


# def hello3(s, n):
#     greeting = "Hello {} ".format(s)
#     print(greeting*n)


# print()
# hello3("Inoske", 2)
# hello3("Nezuko", 4)


def add_list(alist):
    total = 0
    for num in alist:
        total += num
    return total


my_list = [7, 3, 5, 4]
total = add_list(my_list)
print(total)
