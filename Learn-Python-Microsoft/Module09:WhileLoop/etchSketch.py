# Etch a sketch program to draw until the user specifies a line lenght of 0

import turtle

lineLength = 1

while lineLength != 0:
    penColor = input("Enter the Pen Color: ").lower()
    lineLength = int(input("Enter the Line Length: "))
    angleTurn = int(input("Enter the turning angle: "))
    turtle.color(penColor)
    turtle.forward(lineLength)
    turtle.right(angleTurn)



