#10.Salaries
#Given the salaries of three employees working at a department, find the
#amount of money by which the salary of the highest-paid employee differs
#from the salary of the lowest-paid employee. The input consists of three
#positive integers - the salaries of the employees. Output a single number,
#the difference between the top and the bottom salaries

a,b,c = int(input("Write your salary! ")),int(input("Write your salary! ")),int(input("Write your salary! "))

m = a
if m < b:
    m = b
if m < c:
    m = c
max = m
n = a
if n > b:
    n = b
if n > c:
    n = c
min = n

print(max - min)
