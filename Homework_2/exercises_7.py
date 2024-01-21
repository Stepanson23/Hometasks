#9.Line Segment
#You are given four real numbers - the coordinates of two points on a
#plane. The first two numbers are the x and y coordinates of the first point,
#and the last two numbers are the x and y coordinates of the second point.
#Output the length of the line segment bounded by the two points.

x_1,x_2 = float(input("Write the real number!--x_1 ")),float(input("Write the real number!--x_2 "))
y_1,y_2 = float(input("Write the real number!--y_1 ")),float(input("Write the real number!--y_2 "))

l = ((x_1 - x_2)**2 + (y_1 - y_2)**2)**(1/2)
print(l)