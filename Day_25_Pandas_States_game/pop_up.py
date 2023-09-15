from turtle import Turtle, Screen


class Pop_up(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.screen = Screen()

    def get_attempt(self):
        answer_state = self.screen.textinput(
            title=f"{self.counter}/50 States Correct", prompt="What's another state's name?").title()
        return answer_state

    def upgrade_counter(self):
        self.counter += 1

    def already_used(self):
        message = 'This state has already been used \n Push the "OK" button to continue, "Cancel" to exit '
        self.screen.textinput(
            title="Inforamtion Pop-up!", prompt=f"{message}").title()

    def game_over(self):
        message = f"Game Over \nThe states which you don't know has written into a file .csv"
        self.screen.textinput(
            title="Inforamtion Pop-up!", prompt=f"{message}").title()