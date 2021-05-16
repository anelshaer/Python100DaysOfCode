import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

sleep_time = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    if player.is_on_finish_line():
        player.starting_position()
        scoreboard.increase_score()
        car_manager.level_up()

    car_manager.generate_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.xcor() < -300:
            car.hideturtle()
            car_manager.all_cars.remove(car)
        
        # Detect Player Collision
        
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
