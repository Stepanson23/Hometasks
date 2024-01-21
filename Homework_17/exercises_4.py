# ● Character ASCII Values:
# ○ Given a string, create a dictionary where keys are characters, and values are
# their ASCII values.

word = "MAdara"

di = {k:ord(k) for k in word}
print(di)