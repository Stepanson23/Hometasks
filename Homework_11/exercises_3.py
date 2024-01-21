# 3. Write a Python program to check whether a given string is number or
# not using Lambda.


x = input("Write the string! ")
digiit_t_f = lambda x : x.isdigit()
print(digiit_t_f(x))