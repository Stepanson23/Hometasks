# 1. Write a Python program to square and cube every number in a given list of
# integers using Lambda.

numbers = [1,2,3,4,5]
erku_ast = list(map(lambda x: x**2, numbers))
ereq_ast = list(map(lambda x : x**3,numbers))
print(erku_ast,ereq_ast)