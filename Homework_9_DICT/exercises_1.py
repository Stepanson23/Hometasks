# 1.Write a python function, which add a new value with given key in dict.

def dict_new_value(di_1,x):
    
    for i in di_1.keys():
        di_1[i] = x
    return di_1

print(dict_new_value({"a":"Real", "b":"Python", "c":"Is", "d":"Great", "e":"!"}, 15))