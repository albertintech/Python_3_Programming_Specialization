"""Write code that counts the number of words in sentence that contain either an āaā or an āeā. Store the result in the variable num_a_or_e.

Note 1: be sure to not double-count words that contain both an a and an e.

HINT 1: Use the in operator.

HINT 2: You can either use or or elif.

Hard-coded answers will receive no credit."""

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

words = sentence.split()

num_a_or_e = 0
for word in words:
    if 'a' in word or 'e' in word:
        num_a_or_e += 1
print("The number of words with either 'a' or 'e' is:", num_a_or_e)
