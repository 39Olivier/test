import turtle
from random import randint

# region configuration fenetre
fond = (randint(0, 255), randint(0, 255), randint(0, 255))
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(fond)
# endregion

pen_1 = turtle.Turtle()


pen_1.shape('arrow')
length = 100

for i in range(20):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    pen_1.pencolor(color)
    pen_1.forward(150)
    pen_1.left(75)
    pen_1.forward(length)
    pen_1.left(75)
    pen_1.forward(75)
    length = length + 30
wn.exitonclick()
