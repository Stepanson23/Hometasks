#3.Digit Sum
#Input a two-digit natural number and output the sum of its digits. 
#You can assume that the input will be a two-digit number and need not check that programmatically.

n = int(input("Write the number! "))
a = n % 10
b = n // 10
print(a+b)