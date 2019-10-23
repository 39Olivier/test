import turtle
from random import randint

r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

couleur = (r, g, b)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color = couleur
alex.forward(150)
alex.left(90)
alex.forward(75)

alex.color

wn.exitonclick()


