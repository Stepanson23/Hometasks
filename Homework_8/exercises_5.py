# Exercise 5:
# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.

n = int(input())

fib_1 = 0
fib_2 = 1

i = 0
while i < n:
    if fib_1 + fib_2 == i:
        fib_1 = fib_2
        fib_2 = i
        print(fib_2) 
    i += 1
       