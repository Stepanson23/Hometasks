# 5. Write a Python program to add two given lists using map and
# lambda.

x = [1, 2, 3]
y = [4, 5, 6]

print(list(map(lambda x,y: x + y, x, y )))
