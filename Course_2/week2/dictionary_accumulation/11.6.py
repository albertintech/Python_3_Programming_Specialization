"""Accumulating Multiple Results in a Dictionary"""

f = open('lorem_ipsum.txt', 'r')
txt = f.read()

x = {}  # start with an empty directory
x['t'] = 0  # initialize the t counter
x['s'] = 0  # initialize the s counter

# for c in txt:
#     if c == 't':
#         x['t'] += 1  # hard-coded value
#     elif c == 's':
#         x['s'] += 1  # hard-coded value

for c in txt:
    if c == 't':
        x[c] += 1
    elif c == 's':
        x[c] += 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
