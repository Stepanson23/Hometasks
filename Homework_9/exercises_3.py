# 3.Factorial
# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def number_factor(n):
    count = 1
    i = 1
    while i <= n:
        count *= i
        i += 1

    return count

print(number_factor(5))
print(number_factor(6))       