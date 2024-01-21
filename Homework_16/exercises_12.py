# 12. List Exercise:
# Write a function that returns the nth largest element from a list.

def search_elem(n, numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            if numbers[j] < numbers[j+1]:
                (numbers[j+1], numbers[j]) = (numbers[j], numbers[j+1])
    return numbers[n-1]

print(search_elem(2,[1,5,2,9,10,-3]))


