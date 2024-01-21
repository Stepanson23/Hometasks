#8.Three Numbers
#Input three integers. Output the word “Sorted” if the numbers are listed in
#a non-increasing or non-decreasing order and “Unsorted” otherwise.

a,b,c = int(input("Write the number! ")),int(input("Write the number! ")),int(input("Write the number! "))

if (a >= b and b >= c) or (a <= b and b <= c):
    print("Sorted")
else:
    print("Unsorted")    
