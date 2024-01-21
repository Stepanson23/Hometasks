#1.Arrange string characters such that lowercase letters should come first.


word = input()
word_1 = ""
word_2 = ""
for i in word:
    if i.islower():
        word_1 += i
    if i.isupper():
        word_2 += i    
print(word_1 + word_2)            