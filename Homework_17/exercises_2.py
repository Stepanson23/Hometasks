# ● Character Frequency:
# ○ Given a string, create a dictionary where keys are characters and values are their frequencies in the string.


word = "abgabd"

dic = {k:word.count(k) for k in word}
print(dic)