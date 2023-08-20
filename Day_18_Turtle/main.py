from turtle import Turtle, Screen



class Figure():
    def __init__(self, turtle_shape: str, figure_color: str, figure_size: int, angles_amount: int) -> None:
        self.turtle = Turtle()
        self.turtle.shape(turtle_shape)
        self.turtle.color(figure_color)
        self.figure_size = figure_size
        self.angle = int(360 / angles_amount)
        self.steps = angles_amount

    def draw_figure(self) -> None:
        """
        Draws a figure by moving the turtle forward and turning it right.
        """
        for _ in range(self.steps):
            self.turtle.forward(self.figure_size)
            self.turtle.right(self.angle)


figures_data = [

    ("triangle", "green", 100, 3),
    ("square", "red", 100, 4),
    ("turtle", "brown", 100, 5),
    ("classic", "orange", 100, 6),
    ("classic", "yellow", 100, 8),
    ("arrow", "dark blue", 100, 9),
    ("arrow", "dark green", 100, 10),
    ("circle", "blue", 1, 360)

]


for data in figures_data:
    figure = Figure(*data)
    figure.draw_figure()


screen = Screen()
screen.exitonclick()
