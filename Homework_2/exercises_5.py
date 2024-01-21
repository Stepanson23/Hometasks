#7.Birth Year
#The program prompts the user their birth year. Assuming a person’s age
#is a non-negative integer not exceeding 120, output the user’s age or the
#words “Incorrect Year”. The sample outputs assume it’s currently the year
#2016. If you are writing this program during any other year, the correct
#answers may differ. Store the value of the current year in a variable.


year = int(input("Write your year! "))
this_year = 2016
if this_year >= year and year >= this_year - 120:
    age = this_year - year
    print(age)
else:
    print("Incorrect Year")    