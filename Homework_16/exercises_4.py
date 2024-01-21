# 4. List Exercise:
# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)

def two_mass(numbers_1,numbers_2):
    mas_3 = []
    for i in numbers_1:
        for j in numbers_2:
            if i == j:
                mas_3.append(i)
    return mas_3            


print(two_mass([1,2,3],[2,3,4]))