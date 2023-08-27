from turtle import Screen
from snake import Snake
from food import Food
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



food = Food()
snake = Snake()

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
# screen.onkey(snake.reset, "r")
# screen.onkey(snake.extend, "e")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

    # if game.head.distance(food) < 15:
    #     food.refresh()
    #     game.extend()
    # if game.head.xcor() > 280 or game.head.xcor() < -280 or game.head.ycor() > 280 or game.head.ycor() < -280:
    #     game_is_on = False
    #     game.game_over()
    # for segment in game.segments[1:]:
    #     if game.head.distance(segment) < 10:
    #         game_is_on = False
    #         game.game_over()

screen.exitonclick()
