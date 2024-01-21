# 3. List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.

def massiv(numbers):
    sum = 0
    for i in numbers:
        if i % 7 == 0:
            sum += i
    return sum        


print(massiv([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))