from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import keyboard

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "Pong Game"
LEFT_PADDLE_POSITION = (-385, 0)
RIGHT_PADDLE_POSITION = (380, 0)
LEFT_BORDER = -365
RIGHT_BORDER = 360
DISTANCE_TO_PADDLE = 50

# Screen
screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor(f"{BACKGROUND_COLOR}")
screen.title(f"{TITLE}")

ball = Ball()
right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
left_paddle.speed(10)
right_paddle.speed(10)
scoreboard = Scoreboard()
# screen.tracer(0)


# Functions
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
    ball.move()
    # Detect collisions or misses
    ball.check_the_collision()
    if (ball.xcor() > RIGHT_BORDER and ball.distance(right_paddle) < DISTANCE_TO_PADDLE) or (ball.xcor() < LEFT_BORDER and ball.distance(left_paddle) < DISTANCE_TO_PADDLE):
        ball.bounce_x()
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
