# with open('emotion_words.txt', 'r') as ew:
#     for line in ew:
#         print(line.strip())

fileref = open("emotion_words.txt", "r")
contents = fileref.read()
print(contents)
fileref.close()
