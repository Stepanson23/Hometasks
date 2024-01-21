# 4. Write a Python program to find intersection of two given arrays using
# Lambda.



z = lambda l1,l2 : list(filter((lambda a : a in l1,l2),l1,l2))

l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
print(z(l1,l2))
