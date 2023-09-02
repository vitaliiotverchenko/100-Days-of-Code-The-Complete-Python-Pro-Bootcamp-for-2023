import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")
screen.onkey(turtle.move, "W")
screen.onkey(turtle.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    if turtle.ycor() > 280:
        turtle.reset_position()
        cars.level_up()
        # scoreboard.increase_level()w
    if turtle.distance(cars) < 10:
        game_is_on = False
        # scoreboard.game_over()
        time.sleep(2)
        turtle.reset_position()