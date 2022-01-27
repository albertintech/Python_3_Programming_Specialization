"""Dictionary Accumulation"""

f = open('lorem_ipsum.txt', 'r')
txt = f.read()
# txt is now a string of entire char set of lorem_ipsum.txt
t_count = 0  # initialize the accumlator variable
s_count = 0
for c in txt:
    if c == 't':
        t_count += 1  # increment the counter
    elif c == 's':
        s_count += 1
print("t: " + str(t_count) + " occurences")
print("s: " + str(s_count) + " occurences")

# Now, let's use a dictionary!
