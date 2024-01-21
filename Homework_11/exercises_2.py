# 2. Write a Python program to find if a given string starts with a given
# character using Lambda.


x = input("Write the big word! ")
y = input("Write the one element! ")
is_big_str = lambda x,y : x[0] == y
print(is_big_str(x,y))

