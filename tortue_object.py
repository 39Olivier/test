import turtle
from random import randint

wn = turtle.Screen()
Pen_1 = turtle.Turtle()
wn.colormode(255)

color = (randint(0, 255), randint(0, 255), randint(0, 255))

Pen_1.shape('arrow')
Pen_1.pencolor(color)


Pen_1.forward(150)
Pen_1.left(75)
Pen_1.forward(75)
Pen_1.left(75)
Pen_1.forward(75)

wn.exitonclick()
