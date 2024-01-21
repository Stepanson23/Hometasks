#5. Write a Python function to get a string made of 4 copies of the last two characters of a
#specified string (length must be at least 2).
word = input("Write the word! ")
if len(word) >= 2:
    wordResult = word[-2:] * 4
    print(wordResult)