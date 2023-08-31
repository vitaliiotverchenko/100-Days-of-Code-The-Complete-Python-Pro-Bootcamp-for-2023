from turtle import Turtle, Screen
from paddle import Paddle
import keyboard
# classic arcade Pong game

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "Pong Game"
LEFT_PADDLE_POSITION = (-360, 0)
RIGHT_PADDLE_POSITION = (360, 0)

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor(f"{BACKGROUND_COLOR}")
screen.title(f"{TITLE}")
right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)

def check_keys():
    if keyboard.is_pressed('w'):
        left_paddle.go_up()
    if keyboard.is_pressed('s'):
        left_paddle.go_down()
    if keyboard.is_pressed('up'):
        right_paddle.go_up()
    if keyboard.is_pressed('down'):
        right_paddle.go_down()


game_is_on = True
while game_is_on:
    screen.update()
    check_keys()


screen.exitonclick()
