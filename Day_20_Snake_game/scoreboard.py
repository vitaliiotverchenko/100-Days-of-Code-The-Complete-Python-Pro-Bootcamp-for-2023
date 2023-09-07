from turtle import Screen, Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")
TEXT_COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\\Users\\38096\Desktop\\100DaysOfCodeChallenge\\100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2023\\Day_20_Snake_game\\data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.color(f'{TEXT_COLOR}')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    # def game_over(self):
    #     self.color("red")
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align = ALIGMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\\Users\\38096\Desktop\\100DaysOfCodeChallenge\\100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2023\\Day_20_Snake_game\\data.txt", mode='w') as storage:
                storage.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
