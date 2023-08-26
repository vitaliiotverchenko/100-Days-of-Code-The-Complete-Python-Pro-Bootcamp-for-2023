from turtle import Turtle, Screen
import random

race_is_on = True
screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
x = -350
y = 150


for number in range(6):
    random_speed = random.randint(1, 10)
    turtle = Turtle(shape="turtle")
    turtle.color(colors[number])
    turtle.penup()
    turtle.goto(x, y)
    y -= 50
    turtle.speed(random_speed)
    turtles.append(turtle)

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 370:
            race_is_on = False
            if user_bet == turtle.pencolor():
                print(
                    f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {turtle.pencolor()} turtle is the winner!")
        turtle.forward(random.randint(1, 10))

screen.exitonclick()
