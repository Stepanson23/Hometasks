# 2. Write a function in Python to count and display the total number of words in a text file

with open("exercises_2.txt","r") as file:
    x = file.read()
    x_s = x.split(" ")
    x_coun = len(x_s)
    for i in x_s:
        print(i)
        
    print(x_coun)    
   