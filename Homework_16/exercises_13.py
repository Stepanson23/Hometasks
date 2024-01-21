# 13. Sets Exercise:
# Write a function that checks if two sets are disjoint (have no common elements).

def er_sets_disjoint(a,b):
    return a.isdisjoint(b)


a = {1,2,3}
b = {3,5}
print(er_sets_disjoint(a,b))
