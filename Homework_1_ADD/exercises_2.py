# Palindrome Detection:
# Implement a program that checks if a given word is a palindrome (reads the same forwards and backwards)
# using string slicing. For example, if the input is "racecar," the program should print
# "It's a palindrome," and if the input is "python," it should print "It's not a palindrome."


word = input("Write the word! ")
i = len(word) // 2
word_2 = word[i:]
word_3 = word[i + 1 :]
if word[0:i] == word_2[::-1]:
    print("It's a palindrome!")
    exit()
if word[0:i] == word_3[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")
