from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_SPEED = 2

class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.speed(PADDLE_SPEED)
        self.paddle.color(PADDLE_COLOR)
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(position)


    def go_up(self):
        new_y = self.paddle.ycor() + 20 
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

