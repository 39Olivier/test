import turtle
from turtle import *

from random import randint

alex = turtle.Turtle()
speed(0)

bgcolor('black')

x = 1

while x < 400:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    colormode(255)  # this is something that is irrelevant at this point
    # check the pythondocs link at the end for more info

    pencolor(r, g, b)  # changes the color of the pen to the rgb coordinates
    # obtained by the variables r, g, b changing each time

    fd(50 + x)
    rt(90.911)

    x = x + 1

exitonclick()

# again, try to customize  :)

