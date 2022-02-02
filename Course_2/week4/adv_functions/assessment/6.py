def checkingIfIn(a, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]


# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn("cherry")
print(c_false)
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn("cherry", direction=False)
print(c_true)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn("fruit")
print(fruit_ans)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn("eight", d={"eight": 8})
print(param_check)
