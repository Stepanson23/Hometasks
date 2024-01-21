# 4.Write a python function which create dict from 2 lists with the same length

def two_list_dict(li_1,li_2):
    a = {}
    li_1_len = len(li_1)
    for i in range(li_1_len):
        a[li_1[i]] = li_2[i]

    return a        


print(two_list_dict(["a","b","c"],[1,2,3]))
