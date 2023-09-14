from turtle import Turtle, Screen


class Pop_up(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.screen = Screen()

    def get_attempt(self):
        while self.counter < 50:
            answer_state = self.screen.textinput(
                title=f"{self.counter}/50 States Correct", prompt="What's another state's name?").title()
            return answer_state

    def upgrade_counter(self):
        self.counter += 1
