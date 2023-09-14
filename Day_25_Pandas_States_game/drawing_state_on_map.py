from turtle import Turtle


class Draw_state(Turtle):
    def __init__(self,):
        super().__init__()
        self.font = ('Arial', 14, 'normal')
        self.penup()
        self.hideturtle()

    def draw_state(self, name, coordinats):
        self.name = name
        self.coordinats = list(coordinats)
        self.x = self.coordinats[0]
        self.y = self.coordinats[1]
        self.goto(self.x, self.y)
        # self.penup()
        self.write(self.name, font=self.font)
