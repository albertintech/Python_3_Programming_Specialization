
stopwords = ['to', 'a', 'for', 'by', 'an',
             'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org_lst = org.split(" ")
print(org_lst)
acro = ""  # The empty string for the acronym to build
for word in org_lst:
    if word not in stopwords:
        acro += word[0].upper()
print(acro)
