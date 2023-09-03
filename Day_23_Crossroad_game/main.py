import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

# Constants
DISTANCE_TO_CRASH = 18
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

scoreboard = Scoreboard()
turtle = Player()
cars = CarManager()

screen.listen()
screen.onkey(turtle.move, "W")
screen.onkey(turtle.move, "w")


def disable_key_handlers():
    screen.onkey(None, "w")
    screen.onkey(None, "W")


def play_game():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        cars.create_car()
        cars.move_cars()
        if turtle.ycor() > 280:
            turtle.reset_position()
            cars.level_up()
            scoreboard.increase_level()
        for car in cars.all_cars:
            if turtle.distance(car) < DISTANCE_TO_CRASH:
                turtle.collision()
                disable_key_handlers()
                scoreboard.game_over()
                cars.collision()
                game_is_on = False


play_game()
screen.exitonclick()
