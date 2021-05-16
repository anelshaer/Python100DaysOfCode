from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car_chance = random.randint(1, 6)
        if new_car_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_y_pos = random.randint(-250, 250)
            new_car.goto(300, new_y_pos)
            new_len = random.randint(1, 3)
            new_car.shapesize(stretch_wid=1, stretch_len=new_len)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
