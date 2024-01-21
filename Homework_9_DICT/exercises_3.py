# 3.Write a python function, which create a dictionary for given number N,
# where keys are numbers from 1 to N,and 
# values are cubs of that numbers

def create_new_dict(n):
    a ={}
    for i in range(1,n+1):
        a[i] = i**3

    return a



print(create_new_dict(5))
    
    