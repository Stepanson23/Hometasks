# 4.Write a function display_words() in python to read text from a text file "example.txt",
# and display those words, which are less than 4 characters.



def display_words(new_file):
    list_str = new_file.split(" ")
    new_list = []
    for i in list_str:
        if len(i) < 4:
            new_list.append(i)
    return new_list        


f = open("exercises_4.txt","r")
x = f.read()
print(display_words(x))
f.close()