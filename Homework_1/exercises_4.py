#4. Write a Python program to change a given string to a new string where the first and last chars
#have been exchanged.
word = input("Write the word! ")
wordResult = word[-1] + word[1:-1] + word[0]
print(wordResult)