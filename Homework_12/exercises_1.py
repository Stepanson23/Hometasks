# 1.Write a function in python to read the content from a text file "example.txt" line by line
# and display the same on screen.


with open("exercises_1.txt","r") as file:
    for tox in file:
        print(tox)
