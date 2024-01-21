# 2.Write a python program which concat 2 dictionaries.

def concat_new_dict(dict1, dict2): 
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1
       
dict1 = {"a": 10, "b": 8} 
dict2 = {"c": 6, "d": 4}  
print(concat_new_dict(dict1,dict2))