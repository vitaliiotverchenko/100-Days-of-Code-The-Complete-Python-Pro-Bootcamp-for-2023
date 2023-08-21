from turtle import Turtle, Screen, colormode
import random

colormode(255)


class Figure():
    def __init__(self, turtle_shape: str, figure_color: tuple, figure_size: int, angles_amount: int) -> None:
        self.turtle = Turtle()
        self.turtle.speed(10)
        self.turtle.pensize(3)
        self.turtle.shape(turtle_shape)
        self.turtle.color(figure_color)
        self.turtle.figure_size = figure_size
        self.angle = int(360 / angles_amount)
        self.steps = angles_amount
        self.directions = (0, 90, 180, 270)
        self.hirst_colors = [(244, 235, 225), (214, 149, 92), (245, 229, 235), (54, 105, 135), (220, 232, 239), (150, 85, 57), (230, 242, 237), (123, 161, 186), (140, 68, 94), (200, 131, 155), (214, 88, 63), (162, 150, 50), (54,
                                                                                                                                                                                                                                 121, 87), (195, 88, 118), (121, 178, 152), (27, 51, 76), (228, 201, 118), (77, 158, 122), (40, 57, 106), (53, 43, 30), (56, 37, 51), (237, 162, 184), (118, 36, 56), (104, 120, 167), (52, 158, 176), (243, 168, 156), (28, 54, 41), (11, 100, 74), (109, 44, 35), (156, 211, 188)]

    def draw_figure(self) -> None:
        """
        Draws a figure by moving the turtle forward and turning it right.
        """
        for _ in range(self.steps):
            self.turtle.forward(self.figure_size)
            self.turtle.right(self.angle)

    def random_movements_and_colors(self) -> None:
        """
        Randomly moves the turtle.
        """
        for i in range(100):
            self.turtle.color(generate_random_color())
            self.turtle.forward(self.turtle.figure_size)
            self.turtle.setheading(random.choice(self.directions))

    def draws_spirograph(self) -> None:
        """
        Draws a spirograph.
        """
        size_of_the_circle = self.turtle.figure_size
        self.turtle.penup()
        # Переміщення на відстань figure_size
        self.turtle.forward(size_of_the_circle)
        self.turtle.pendown()

        for _ in range(int(360 / self.angle)):
            self.turtle.color(generate_random_color())
            self.turtle.circle(size_of_the_circle)
            self.turtle.setheading(self.turtle.heading() + self.angle)
        # for _ in range(int(360 / self.angle)):
        #     self.turtle.color(generate_random_color())
        #     self.turtle.circle(self.turtle.figure_size)
        #     self.turtle.setheading(self.turtle.heading() + self.angle)

    def draw_a_hirst_painting(self, dots_in_a_row: int, lines_amount: int, dot_size: int, space_between_d: int) -> None:
        """
        Draws a hirst painting.
        """
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setpos(-350, +350)
        for _ in range(lines_amount):
            for _ in range(dots_in_a_row):
                self.turtle.dot(dot_size, random.choice(self.hirst_colors))
                self.turtle.forward(space_between_d)
            self.turtle.backward(space_between_d * dots_in_a_row)
            self.turtle.right(90)
            self.turtle.forward(dot_size * 2)
            self.turtle.left(90)


# figures_data = [

#     ("triangle", "green", 100, 3),
#     ("square", "red", 100, 4),
#     ("turtle", "brown", 100, 5),
#     ("classic", "orange", 100, 6),
#     ("classic", "yellow", 100, 8),
#     ("arrow", "dark blue", 100, 9),
#     ("arrow", "dark green", 100, 10),
#     ("circle", "blue", 1, 360)

# ]

turtle_shape = ("arrow", "turtle", "circle", "square", "triangle", "classic")


# for data in figures_data:
#     figure = Figure(*data)
#     figure.draw_figure()


def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


# random_shape = random.choice(turtle_shape)
# random_color = generate_random_color()
# # line = Figure(random_shape, random_color, 100, random.randint(3, 10))
# line = Figure(random_shape, random_color, 100, 50)
# # line.random_movements_and_colors()
# line.draws_spirograph()


hirst = Figure("classic", (255, 15, 15), 10, 360)
hirst.draw_a_hirst_painting(10, 10, 20, 50)
screen = Screen()
screen.exitonclick()
