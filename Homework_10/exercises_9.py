# Exercise 9: Print Prime Numbers Function
# Write a function that prints all prime numbers up to a given limit.

def prost_chis(n):
    a = list(range(n+1)) 
    a[1] = 0       
    list_1 = []      
    i = 2
    while i <= n:     
        if a[i] != 0:
            list_1.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return list_1



print(prost_chis(100))    