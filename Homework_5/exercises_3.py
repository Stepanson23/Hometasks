#3.Write a program to check if two strings are balanced. For example, strings s1 and
#s2 are balanced if all the characters in the s1 are present in s2. The character’s
#position doesn’t matter.

s_1 = input()
s_2 = input()
sum = 0
for i in s_1:
    if i in s_2:
        sum += 1
    
if sum == len(s_1):
    print(True)
else:
    print(False)    
                