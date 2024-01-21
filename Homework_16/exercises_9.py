# 9. Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary.


def maximum(libra):
    max = 0
    ki = 0
    for k in libra.keys():
        if libra[k] > max:
            max = libra[k]
            ki = k
    return ki        




print(maximum({"Valod":15,"Igor":12,"Stepan":19}))    