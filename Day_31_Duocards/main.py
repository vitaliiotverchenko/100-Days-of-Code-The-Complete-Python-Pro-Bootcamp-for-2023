import tkinter as tk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_IMAGE = "Day_31_Duocards/images/card_front.png"
CARD_BACK_IMAGE = "Day_31_Duocards/images/card_back.png"
RIGHT_BUTTON_IMAGE = "Day_31_Duocards/images/right.png"
WRONG_BUTTON_IMAGE = "Day_31_Duocards/images/wrong.png"
CURRENT_LANGUAGE = "English"
WORD = 'Start'

# ------------------ READ CSV DATA --------------
data_frame = pd.read_csv("Day_31_Duocards/2000_words_en_ru.csv")
dictionary = data_frame.to_dict(orient="records")
# print(dictionary)

# ----------------GENERATING RANDOM WORDS---------


def next_card():
    current_card = random.choice(dictionary)
    canvas.itemconfig(language_label, text="English")
    canvas.itemconfig(word_label, text=current_card["English"])


# ----------------- UI SETUP ------------------
window = tk.Tk()
window.title("Duocards")
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526,
                   bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file=CARD_FRONT_IMAGE)
canvas.create_image(400, 263, image=card_front)
language_label = canvas.create_text(
    400, 150, text='Language', font=("Arial", 40, "italic"))
word_label = canvas.create_text(
    400, 263, text='Word', font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# ------------- BUTTONS -------------------
known_button_image = tk.PhotoImage(file='Day_31_Duocards\images\\right.png')
known_button = tk.Button(image=known_button_image,
                         highlightthickness=0, borderwidth=0, command=next_card)
known_button.grid(column=0, row=1, sticky='n')


unknown_button_image = tk.PhotoImage(file="Day_31_Duocards/images/wrong.png")
unknown_button = tk.Button(image=unknown_button_image,
                           highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(column=1, row=1,  sticky='n')

next_card()
window.mainloop()
