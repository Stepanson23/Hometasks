#1.

def chek_pangram(str_1):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for tar in alpha:
        if tar not in str_1.lower():
            return False
 
    return True                


print(chek_pangram("Alpha"))
print(chek_pangram("abcdefghijKlmnopqrstuvwxyz"))
print(chek_pangram(input("Write your pongramm sentence! ")))