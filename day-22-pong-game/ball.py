from turtle import Turtle

MOVEMENT_DISTANCE = 20
# https://www.101computing.net/bouncing-algorithm/


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10        

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()

    def reset(self):
        self.goto(0, 0)
        self.x_move = 10
        self.bounce_x()

    def increase_speed(self):
        self.x_move *= 1.1
