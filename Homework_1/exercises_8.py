#8.Create a string made of the first, middle and last character of given string with odd number of
#symbols.

word = input("Write the word! ")
length = len(word)
if length % 2 == 1:
    i = length // 2
    print(word[0] + word[i] + word[-1])    
else:
    print("Good by!")    










