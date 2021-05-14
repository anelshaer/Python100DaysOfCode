import colorgram
import turtle
import random

IMAGE = '739020dac9684b7d0ca4430ce06106b4.jpg'
DIRECTIONS = [0, 90, 180, 270]


def extract_colors(image, number_of_colors):
    colors = colorgram.extract(image, number_of_colors)
    rgb_colors = [tuple(color.rgb) for color in colors]
    return rgb_colors


COLORS_LIST = extract_colors(IMAGE, 100)


def get_random_color():
    return random.choice(COLORS_LIST)


def setposition(turtle_obj, x, y):
    turtle_obj.penup()
    turtle_obj.setposition(x, y)


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
    my_turtle = turtle.Turtle()
    my_turtle.shape("triangle")
    my_turtle.hideturtle()
    pos_x = pos_y = -200
    number_of_dots = 100
    paint(my_turtle, number_of_dots, pos_x, pos_y)
    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
