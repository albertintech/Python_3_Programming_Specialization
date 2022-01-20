stopwords = ['to', 'a', 'for', 'by', 'an',
             'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent_lst = sent.split(" ")
print(sent_lst)
acro = ""  # The empty string for the acronym to build
counter = 0
for word in sent_lst:
    if word not in stopwords:
        if counter == 0:
            acro += word[0].upper() + word[1].upper()
            counter += 1
        else:
            acro += ". " + word[0].upper() + word[1].upper()
            counter += 1
print(acro)
