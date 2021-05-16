from turtle import Turtle
from typing import List


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color('red')
        self.starting_position()

    def starting_position(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_on_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
