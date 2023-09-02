from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        # time.sleep(1)
        self.showturtle()
        self.move_speed = 0.1
        self.bounce_x()

    def check_the_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
        # if self.xcor() > 380 or self.xcor() < -380:
        #     self.reset_position()   