from turtle import Turtle
import time

MOVE_DISTANCE = 15
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
HEAD_SHAPE = "triangle"
BODY_SHAPE = "square"
COLOR = "white"
SNAKE_BODY_LENGTH = 4


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]
        self.head.shape(HEAD_SHAPE)

    def _create_snake(self) -> None:
        for _ in range(SNAKE_BODY_LENGTH):
            self.add_segment()

    def add_segment(self) -> None:
        segment = Turtle(shape=BODY_SHAPE)
        segment.color(COLOR)
        segment.pensize(20)
        segment.penup()
        self.segments.append(segment)
        prvious = self.segments[-1]
        segment.goto((
                      prvious.xcor() +
                      prvious.pensize(),
                      prvious.ycor()))

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self._create_snake()
        self.head = self.segments[0]
        self.head.shape(HEAD_SHAPE)
