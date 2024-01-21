#12.Line Segment Intersection
#You are given four real numbers- a1, b1, a2, b2 - The endpoints of two line segments on a line. 
#Find the length of their intersection. Note that the order of the endpoints of a segment is irrelevant, 
#i.e. the segments [1;2] and [2;1] are considered the same.

a_1,a_2 = float(input("Write the number! ")),float(input("Write the number! "))
b_1,b_2 = float(input("Write the number! ")),float(input("Write the number! "))

max = a_1
min_2 = a_2
max_2 = b_2

if max < b_1:
    max = b_1
if min_2 > b_2:
    min_2 = b_2
    max_2 = a_2

if max > min_2:
    if max > max_2:
         print(max_2 - min_2)
         exit()
    print(max - min_2)
else:
    print(0)