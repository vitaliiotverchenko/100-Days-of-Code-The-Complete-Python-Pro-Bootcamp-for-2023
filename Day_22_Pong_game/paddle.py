from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_SPEED = 2

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(PADDLE_SPEED)
        self.color(PADDLE_COLOR)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 20 
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

