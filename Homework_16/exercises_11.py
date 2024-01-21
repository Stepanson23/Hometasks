# 11. Function Exercise:
# Write a function that checks if a given string is a valid email address

email = input()
a = email.index("@")
b = email.index(".")
if len(email) >= 8 and len(email) > b+1 and email.count("@") == 1 and email.count(".") == 1:
    if a != 0 and b != a+1:
        print("Valid mail")
    else:
        print("Invalid mail")
else:
    print("Invalid mail")