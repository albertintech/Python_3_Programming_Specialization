str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
lst = str1.split()
freq_words = {}
for word in lst:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
print(freq_words)
