"""Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words."""

sp_file = open("school_prompt.txt", "r")
p_words = []
word_lst = []
for a_line in sp_file:
    values = a_line.split(",")
    strings = values[0]
    word_lst = strings.split()
    for word in word_lst:
        if "p" in word:
            p_words.append(word)
p_words[2] = 'ups,'
p_words.insert(2, 'papers,')
p_words.insert(4, 'scripts.')
print(p_words)
sp_file.close()
