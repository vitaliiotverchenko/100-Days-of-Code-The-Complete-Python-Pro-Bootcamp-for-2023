import turtle
from pop_up import Pop_up
from states_data import Data_states
from drawing_state_on_map import Draw_state

PATH = "Day_25_Pandas_States_Game/50_states.csv"
draw_state = Draw_state()
pop_up = Pop_up()
data = Data_states(PATH)
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_25_Pandas_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
used_states = set()


def game():
    game_is_on = True
    while game_is_on:
        answer = pop_up.get_attempt()
        if answer == "Exit":
            game_is_on = False
        elif data.check_state(answer) and answer not in used_states:
            used_states.add(answer)
            pop_up.upgrade_counter()
            x_y = data.return_x_y(answer)
            draw_state.draw_state(answer, x_y)
        elif answer in used_states:
            pop_up.already_used()


game()

turtle.mainloop()
