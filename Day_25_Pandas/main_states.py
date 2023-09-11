import turtle
# from states_list import states
# from pop_up import Pop_up

screen = turtle.Screen()
screen.title('US states game')
image = 'Day_25_Pandas\\blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
# pop_up = Pop_up()

def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)


# def play_game():
#     game_is_on = True
#     while game_is_on:
#         state = pop_up.get_answer()
#         if state == 'exit':
#             game_is_on = False
#         pop_up.check_answer(state)

# play_game()

turtle.mainloop()
