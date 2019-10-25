import turtle
from random import randint


def tuple_random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(tuple_random_rgb())

pen_1 = turtle.Turtle()
pen_1.shape('arrow')
length = 100

for i in range(10):
    color = tuple_random_rgb()
    pen_1.pencolor(color)
    pen_1.pensize(10)
    pen_1.speed(5)
    # pen_1.circle(50, 150)
    pen_1.forward(150)
    pen_1.left(75)
    pen_1.forward(length)
    pen_1.left(75)
    pen_1.forward(75)
    length = length + 30

wn.exitonclick()
