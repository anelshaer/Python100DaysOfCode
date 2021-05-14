from turtle import Turtle, Screen, exitonclick
from random import random

my_turtle = Turtle()
my_turtle.shape("turtle")


def get_random_color():
    return (random(), random(), random())


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.pen(pencolor=get_random_color(), pensize=1, speed="fastest")
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)


draw_spirograph(5)

Screen()
exitonclick()
