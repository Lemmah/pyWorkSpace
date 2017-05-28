# Polygon Drawer.
# Created by James Lemayian
# This program draws a polygon with the sides specified by the user
# using the turtle library

import turtle
print("\nThis program will draw a polygon of user specified number of sides using the turtle library.\n")
sides = int(input("Input the number of sides: "))

for line in range(sides):
    turtle.forward(100)
    turtle.left(360/sides)
    for smaller_lines in range(sides):
        turtle.forward(50)
        turtle.left(360/sides)
