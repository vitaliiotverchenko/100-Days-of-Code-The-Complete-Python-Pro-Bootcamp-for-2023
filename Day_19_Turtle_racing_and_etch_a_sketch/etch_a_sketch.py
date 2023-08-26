from turtle import Turtle, Screen
leonardo = Turtle()
screen = Screen()


def move_forward():
    leonardo.forward(10)


def move_backward():
    leonardo.backward(10)


def move_left():
    leonardo.left(10)


def move_right():
    leonardo.right(10)


def clear_screen():
    leonardo.clear()
    leonardo.penup()
    leonardo.home()
    leonardo.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
