#3.
def tvab_mij(number):
    sum = 0
    for i in number:
        sum += i
    return sum/len(number)

print(tvab_mij([1,2,3,4]))    
