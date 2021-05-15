from turtle import Turtle
MOVEMENT_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.color("white")
        self.left(90)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(MOVEMENT_DISTANCE)

    def move_down(self):
        if self.ycor() > -240:
            self.forward(-MOVEMENT_DISTANCE)
