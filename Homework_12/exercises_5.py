# 5. Write a python program to read a file, a.txt line by line.

with open("exercises_5.txt","r") as file: 
    for tox in file:
        print(tox)