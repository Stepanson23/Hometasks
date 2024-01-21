# 1.Max of Three
# Write a Python function to find the Max of three numbers.

def max_number(a,b,c):
    li_1 = [a,b,c]
    x = li_1[0]
    for i in li_1:
        if i > x:
            x = i
    return x

print(max_number(1,2,6))        
