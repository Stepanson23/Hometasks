#2.Count all letters, digits, and special symbols from a given string

word = input()
tiv = 0
tar = 0
sim = 0

for i in word:
    if(ord(i) >= 48 and ord(i) <= 57): 
       tiv = tiv + 1 
    elif((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
        tar = tar + 1
    else:
        sim = sim + 1        
print(f"chars = {tar}, digits = {tiv}, symbol = {sim}:")  