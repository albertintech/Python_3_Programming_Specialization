sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
lst = sent.split()
wrd_d = {}
for word in lst:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1
print(wrd_d)
