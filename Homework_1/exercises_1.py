#1. Write a Python program to get a string made of the first 2 and the last 2 chars from a
#given string.
 
word = input("Write the word! ")
wordResult = word[:2] + word[-2:]
print(wordResult)