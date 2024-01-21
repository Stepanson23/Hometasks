# Exercise 4:
# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.

import random

rand_number = random.randint(1,100)
n = int(input())
while n != rand_number:
    if n < rand_number: 
        n = int(input("Bardzr Tiv asa! "))
    elif n > rand_number:
        n = int(input("Cacr tiv asa! "))    