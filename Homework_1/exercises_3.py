#3. Write a Python program to remove the n-th index character from a nonempty string.
word = input("Write the word! ")
i = int(input("Write the index! "))
if i < len(word):
    print(word[:i]+word[i+1:])
else:
    print("Good by!")    