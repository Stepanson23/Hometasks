# 9. Append new string in the middle of a given (even number of characters) string.

word = input("Write the word! ")
wordNew = input("Write the new word! ")
length = len(word)
if length % 2 == 0:
    i = length // 2
    print(word[:i] + wordNew + word[i:])
else:
    print("Good by!")
