# Exercise 4:
# Print the multiplication table of 5 using a for loop and f”strings”. The table should be
# printed up to 10.

for i in range(1, 11):

    for j in range(1, 11):
        
        print(f"{i}*{j} = {i * j}")

    print(" ")    