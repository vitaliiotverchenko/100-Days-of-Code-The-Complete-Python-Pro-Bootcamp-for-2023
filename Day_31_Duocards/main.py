import tkinter as tk
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_IMAGE = "Day_31_Duocards/images/card_front.png"
CARD_BACK_IMAGE = "Day_31_Duocards/images/card_back.png"
RIGHT_BUTTON_IMAGE = "Day_31_Duocards/images/right.png"
WRONG_BUTTON_IMAGE = "Day_31_Duocards/images/wrong.png"
CURRENT_LANGUAGE = "English"
WORD = 'Start'
# Time in miliseconds between flips of the card
TIME_TO_WAIT = 5000
current_card = {}
to_learn = {}


# ------------------ READ CSV DATA --------------
# try to open words_to_learn.csv if it exists

try:
    original_data = pd.read_csv("Day_31_Duocards/words_to_learn.csv")
except FileNotFoundError:
    # if not, open 2000_words_en_ru.csv
    original_data = pd.read_csv("Day_31_Duocards/2000_words_en_ru.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = original_data.to_dict(orient="records")

# ----------------GENERATING RANDOM WORDS---------


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_label, text="Russian", fill="black")
    canvas.itemconfig(word_label, text=current_card
                      ["Russian"], fill="black")
    flip_timer = window.after(5000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv(
        "Day_31_Duocards/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    # global  flip_timer
    # window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(
        word_label, text=current_card["English"], fill="white")


# ----------------- UI SETUP ------------------
window = tk.Tk()
window.title("Duocards")
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(TIME_TO_WAIT, func=flip_card)

canvas = tk.Canvas(width=800, height=526,
                   bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file=CARD_FRONT_IMAGE)
card_back = tk.PhotoImage(file=CARD_BACK_IMAGE)
canvas_image = canvas.create_image(400, 263, image=card_front)
language_label = canvas.create_text(
    400, 150, text='Language', font=("Arial", 40, "italic"))
word_label = canvas.create_text(
    400, 263, text='Word', font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# ------------- BUTTONS -------------------#
known_button_image = tk.PhotoImage(file='Day_31_Duocards\images\\right.png')
known_button = tk.Button(image=known_button_image,
                         highlightthickness=0, borderwidth=0, command=is_known)
known_button.grid(column=0, row=1, sticky='n')


unknown_button_image = tk.PhotoImage(file="Day_31_Duocards/images/wrong.png")
unknown_button = tk.Button(image=unknown_button_image,
                           highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(column=1, row=1,  sticky='n')

next_card()
window.mainloop()
