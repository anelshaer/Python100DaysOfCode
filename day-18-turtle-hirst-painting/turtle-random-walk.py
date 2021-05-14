from turtle import Turtle, Screen, exitonclick
import random

my_turtle = Turtle()
my_turtle.shape("triangle")
direction = [0, 90, 180, 270]


def get_random_color():
    return (random.random(), random.random(), random.random())


for _ in range(10000):
    my_turtle.pen(pencolor=get_random_color(), pensize=15, speed=8)
    my_turtle.setheading(random.choice(direction))
    my_turtle.forward(30)

Screen()
exitonclick()
