# ● Random Password Generator:
# ○ Write a function that generates a random password for the user. Allow the user
# to specify the length and complexity of the password (include letters, numbers,
# and symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation, )

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


print(pasword_generator(10))
print(pasword_generator(8))