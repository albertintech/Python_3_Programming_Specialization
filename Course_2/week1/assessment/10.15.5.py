"""We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words."""

fileref = open("emotion_words.txt", "r")
contents = fileref.read()
word_lst = []
word_lst = contents.split()
print(len(word_lst))
fileref.close()
