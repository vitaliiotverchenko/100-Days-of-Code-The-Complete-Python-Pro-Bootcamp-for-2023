from turtle import Turtle, Screen
import random
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.segments = []
        self.create_snake()
        self.game_is_on = True

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=(-20 * i), y=0)
            self.segments.append(new_segment)

    def move(self):
        self.screen.update()
        time.sleep(0.2)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(0, 0)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)

    def create_food(self):
        food = Turtle("square")
        food.color("red")
        food.penup()
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.food = food
        self.screen.update()

    def play(self):
        while self.game_is_on:
            self.move()
            self.screen.listen()
            self.screen.onkey(self.up, "w")
            self.screen.onkey(self.up, "Up")
            self.screen.onkey(self.down, "s")
            self.screen.onkey(self.down, "Down")
            self.screen.onkey(self.left, "a")
            self.screen.onkey(self.left, "Left")
            self.screen.onkey(self.right, "d")
            self.screen.onkey(self.right, "Right")
            self.screen.onkey(self.reset, "r")
            self.screen.onkey(self.extend, "e")


game = Snake()
game.play()
screen.listen()

screen.exitonclick()
