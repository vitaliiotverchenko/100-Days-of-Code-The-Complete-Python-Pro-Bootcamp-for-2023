from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"
TITLE = "My Snake Game"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(f"{SCREEN_BG_COLOR}")
screen.title(f"{TITLE}")
screen.tracer(0)


food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "W")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "S")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "A")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "D")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
