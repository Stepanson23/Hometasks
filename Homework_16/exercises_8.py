# 8. Dictionaries Exercise:
# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.

name = input()
def libra(bibl):
    for k in bibl.keys():
        if name == bibl[k]:
            return k
    return "No book"    

print(libra({"Vayna i mir":"Lev Tolstoy","Starik i more":"Ernest Heminguey"}))
