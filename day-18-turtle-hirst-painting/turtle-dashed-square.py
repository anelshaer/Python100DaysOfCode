from turtle import Turtle, Screen, exitonclick

my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.color('red')

for _ in range(4):
    for i in range(10):
        if i % 2 == 0:
            my_turtle.penup()
        else:
            my_turtle.pendown()
        my_turtle.forward(10)
    my_turtle.right(90)


Screen()
exitonclick()
