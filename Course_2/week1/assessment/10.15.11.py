"""Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words."""

p_words = ['topics', 'point', 'papers', 'ups', 'cat', 'zoo']
p_list = []
with open('emotion_words.txt', 'r') as sp:
    for line in sp:
        print(line)
#         for word in line:
#             if 'p' in word:
#                 p_words.append(word)
# print(p_words)

# for word in p_words:
#     if 'p' in word:
#         p_list.append(word)
# print(p_list)
