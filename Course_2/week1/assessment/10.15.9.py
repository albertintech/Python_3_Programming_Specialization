'''Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.'''

ew_file = open("emotion_words.txt", "r")
emotions = []
for a_line in ew_file:
    values = a_line.split(",")
    strings = values[0]
    emotions.append(strings.split()[0])

print(emotions)
ew_file.close()
