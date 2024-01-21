# Exercise 3:
# Write a Python program that calculates the sum of all even numbers between 1 and 100
# using a while loop.

i = 1
resul = 0
while i < 100:
    if i % 2 == 0:
        resul += i
    i += 1

print(resul)    