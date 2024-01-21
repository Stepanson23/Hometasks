# ● Password Checker:
# ○ Write a function that will get a function string and check if the password is strong or not.
# Strong password must contain | One uppercase letter | one special symbol | one number
# Length of the password should be 8 or more
# If your password is Strong you will return True. else return False

import random,string

def pasword_generator(erk):
    low = string.ascii_lowercase
    up = string.ascii_uppercase
    sym = string.punctuation
    num = string.digits

    ynd = low + up + sym + num
    x = random.sample(ynd,erk)
    pas = "".join(x)
    return pas

def pas_true_or_false(gen_str):
    n = len(gen_str)
    norm = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    upper = list(filter(lambda x: x.isupper(),gen_str[0]))
    erk = lambda x : x >= 8 
    for i in range(1,n):
        lower = list(filter(lambda x: x.islower(),gen_str[i]))
        digit = list(filter(lambda x: x.isdigit(),gen_str[i]))
        symb = list(filter(lambda x: x not in norm,gen_str[i]))    
    if lower and upper and digit and symb and erk(n):
        return True
    else:
        return False 

gen_str = pasword_generator(10)
print(gen_str)
print(pas_true_or_false(gen_str))    