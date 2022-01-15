"""
addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
"""

addition_str = "2+5+10+20"
""" 
input = string
output = integer
Req = Integer output must be sum of all ints in string
Algo:
Take in string
Split on '+'
Iterate through list of string ints
Cast each string to int
Accumulate int values into sum_value
"""
sum_val = 0
split_str = addition_str.split('+')
# print(split_str)
for i in split_str:
    sum_val = sum_val + int(i)
print(sum_val)
