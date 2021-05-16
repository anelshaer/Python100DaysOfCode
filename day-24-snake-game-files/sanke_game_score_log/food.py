from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "green"
SPEED = 'fastest'


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.speed(SPEED)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self) -> None:
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
