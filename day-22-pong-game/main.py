from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE_POSITION = (350, 0)
LEFT_PADDLE_POSITION = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game!")
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()  
    # Detect Collision with Paddle
    if (ball.xcor() > 320 and right_paddle.distance(ball) < 50) or (ball.xcor() < -320 and left_paddle.distance(ball) < 50):
        ball.bounce_x()
        ball.increase_speed()
    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect Right Paddle miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    # Detect Left Paddle miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
