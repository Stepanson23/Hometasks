#4.

def index_find(lister,n):
    j = 0
    for i in lister:
        if i == n:
            return j
        j += 1
    return -1

print(index_find([1,2,3,4,5],5))
print(index_find([1,2,3,4,5],6))
