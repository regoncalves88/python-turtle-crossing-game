import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
loop_counter = 6

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loop_counter % 6 == 0:
        car_manager.create_car()

    car_manager.move_cars()

    loop_counter += 1

screen.exitonclick()
