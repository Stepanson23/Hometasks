# 2.Letters Count
# Write a Python function to calculate count of each letter in string
#{a: 5, b: 2, r: 2, k: 1, d: 1}
def count_letters(str_count):
    d_1 = {}
    for i in str_count:
        kluch = d_1.keys()
        if i in kluch:
            d_1[i] += 1
        else:
            d_1[i] = 1

    return d_1        

print(count_letters("abrakadabra"))