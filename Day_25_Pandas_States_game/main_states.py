import turtle
import pandas as pd
from pop_up import Pop_up


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
        print(answer)


        # answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
        # if answer_state == "Exit":
        #     game_is_on = False
        # else:
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
