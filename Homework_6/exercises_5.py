# Exercise 5:
# You are given three lists, list1, list2, and list3. Your task is to implement a
# programm that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all
# three.
# The set of elements that are unique to each list (present in only one list).

a = input().split()
b = input().split()
c = input().split()

print(set(a) & set(b) & set(c))

print((set(a) | set(b) | set(c))-(set(a) ^ set(b) ^ set(c)))

print((set(a) | set(b) | set(c)) - ((set(a) | set(b) | set(c))-(set(a) ^ set(b) ^ set(c)))-(set(a) & set(b) & set(c)))