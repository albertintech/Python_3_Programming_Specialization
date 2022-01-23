"""Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt."""

fileref = open("emotion_words2.txt", "r")
contents = fileref.read()
first_forty = contents[:40]
print(contents)
print(first_forty)
fileref.close()
