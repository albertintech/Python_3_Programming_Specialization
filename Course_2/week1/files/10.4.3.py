"""Without using the len method, write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines."""

ewords = open("emotion_words.txt", "r")
count = 0
for line in ewords:
    count += 1
num_lines = count
print(num_lines)
