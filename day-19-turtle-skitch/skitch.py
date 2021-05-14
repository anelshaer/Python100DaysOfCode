import colorgram
import turtle
import random


def get_random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)


def setposition(turtle_obj, x, y):
    turtle_obj.penup()
    turtle_obj.setposition(x, y)


def clear_screen():
    global my_turtle
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


def move_forward():
    global my_turtle
    my_turtle.forward(10)


def move_backward():
    global my_turtle
    my_turtle.forward(-10)


def turn_right():
    global my_turtle
    my_turtle.setheading(my_turtle.heading() + 10)


def turn_left():
    global my_turtle
    my_turtle.setheading(my_turtle.heading() - 10)


def paint(my_turtle, number_of_dots, pos_x, pos_y):
    """Painting a Hirst Paint, takes turtle object, number of dots,
    and position of where to start"""
    for dot_count in range(number_of_dots):
        if dot_count % 10 == 0:
            setposition(my_turtle, pos_x, pos_y)
            pos_y += 50
        my_turtle.dot(20, get_random_color())
        my_turtle.forward(50)


def main():
    turtle.colormode(255)
    # my_turtle = turtle.Turtle()
    global my_turtle
    my_turtle.shape("triangle")
    screen = turtle.Screen()
    screen.listen()    
    screen.onkeypress(key='w', fun=move_forward)
    screen.onkeypress(key='s', fun=move_backward)
    screen.onkeypress(key='a', fun=turn_left)
    screen.onkeypress(key='d', fun=turn_right)
    screen.onkeypress(key='c', fun=clear_screen)
    screen.exitonclick()

my_turtle = turtle.Turtle()

if __name__ == "__main__":
    main()
