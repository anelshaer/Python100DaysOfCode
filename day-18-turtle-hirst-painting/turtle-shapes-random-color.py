from turtle import Turtle, Screen, exitonclick
from random import random

my_turtle = Turtle()
my_turtle.shape("triangle")


def draw_shape(sides):
    my_turtle.pen(pensize=8, speed=8)
    my_turtle.color(random(), random(), random())
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.left(360/sides)


for sides in range(3, 20):
    draw_shape(sides)

Screen()
exitonclick()
