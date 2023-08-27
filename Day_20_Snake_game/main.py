from turtle import Screen
from snake import Snake
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


game = Snake()
game.play()
screen.listen()

screen.exitonclick()
