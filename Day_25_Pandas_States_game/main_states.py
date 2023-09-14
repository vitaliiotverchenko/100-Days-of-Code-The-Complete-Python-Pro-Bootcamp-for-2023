import turtle
from pop_up import Pop_up
from states_data import Data_states


path = "Day_25_Pandas_States_Game/50_states.csv"
data = Data_states(path)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_25_Pandas_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pop_up = Pop_up()


def game():
    game_is_on = True
    while game_is_on:
        answer = pop_up.get_attempt()
        if answer == "Exit":
            game_is_on = False
        elif data.check_state(answer):
            pop_up.upgrade_counter()



        #     for state in states:
        #         if state == answer_state:
        #             print(state)
        #             t = turtle.Turtle()
        #             t.hideturtle()
        #             t.penup()
        #             t.goto(int(states[state]["x"]), int(states[state]["y"]))
        #             t.write(state)
        #             break

        # answer_state = screen.textinput(
        #     title="Guess the State", prompt="What's another state's name?").title()
        # print(answer_state)


game()

turtle.mainloop()
