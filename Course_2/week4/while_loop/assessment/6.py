# Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing

def beginning(lst):
    sublst = []
    n = 0
    while n < len(lst) and n < 10:
        if lst[n] == "bye":
            break
        else:
            sublst.append(lst[n])
        n += 1
    return sublst


words = ["go", "x", "y", "j", "a", "bye", "to", "so", "d", "quark", "z", "by"]
a = beginning(words)
print(a)
