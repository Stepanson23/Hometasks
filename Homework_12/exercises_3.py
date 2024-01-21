# 3. Write a python program to add text to a file and display the text in python.txt.

f = open("exercises_3.txt","a")
f.write("learn Python!")
f.close()
x = open("exercises_3.txt","r")
print(x.read())
x.close()
