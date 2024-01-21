# ● Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.

words = ["Madara", "Itachi", "Orochimaru", "Kim", "Na"]

dic = {k:len(k) for k in words if len(k) > 3}
print(dic)