import turtle

screen = turtle.Screen()
screen.title('US states game')
image = 'Day_25_Pandas\\blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
def get_mouse_click_coor(x,y):
   print (x,y)
turtle.onscreenclick(get_mouse_click_coor)

answer_state = turtle.textinput(title='Guess the state', prompt='Whats another state name?')
print(answer_state)





turtle.mainloop()

