"""Scratch file for Week 3 of Python 3 Basics"""

x = 15

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]
output = ""
if "SI 106" in courses:
    output = "You can apply to SI!"
else:
    output = "Take SI 106!"
print(output)

a = 20
b = 15
if b > a:
    a *= 2
c = b + a

x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
elif x == 0:
    print(x, " is a positive number")
else:
    print("This is always printed")

x = 3
y = 5
z = 2
if x < y and x < z:
    print("a")
elif y < x and y < z:
    print("b")
else:
    print("c")

str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "false" in str1:
    output = "False. You aren't you?"
elif "true" in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false!"
print(output)
