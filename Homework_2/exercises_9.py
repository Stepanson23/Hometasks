#11.Rounding - 2
#Given a real number, round it to the nearest whole.

a = float(input("Write the number! "))
b = int(a)
if a - b > 0.5:
    print(int(a) + 1)
else:
    print(int(a))     

