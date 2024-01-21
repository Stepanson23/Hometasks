# ● Vowels in a Word:
# ○ Create a list of vowels present in a given word.

word = input()
st = "AEIOUYaeiouy"

glas = [x for x in word if x in st]
print(glas)
