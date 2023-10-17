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

# ------------------ READ CSV DATA --------------
data_frame = pd.read_csv("Day_31_Duocards/2000_words_en_ru.csv")
dictionary = data_frame.to_dict(orient="records")
# print(dictionary)

# ----------------GENERATING RANDOM WORDS---------


def next_card():
    canvas.itemconfig(canvas_image, image=card_front)
    current_card = random.choice(dictionary)
    canvas.itemconfig(language_label, text="Russian", fill="black")
    canvas.itemconfig(timer_label, fill="black")

    canvas.itemconfig(word_label, text=current_card
                      ["Russian"], fill="black")

    def english_word():
        canvas.itemconfig(language_label, text="English", fill="white")
        canvas.itemconfig(
            word_label, text=current_card["English"], fill="white")
        canvas.itemconfig(timer_label, fill="white")

    # timer counting time from 5 to 0
    def count_down(count):
        canvas.itemconfig(timer_label, text=count)
        if count > 0:
            window.after(1000, count_down, count - 1)
        else:
            # change card image to the card_back.png
            canvas.itemconfig(canvas_image, image=card_back)
            english_word()
    count_down(5)
    # after 5 seconds flip the card
    # window.after(5000, func=russian_translation)


# ----------------- UI SETUP ------------------
window = tk.Tk()
window.title("Duocards")
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526,
                   bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file=CARD_FRONT_IMAGE)
card_back = tk.PhotoImage(file=CARD_BACK_IMAGE)
canvas_image = canvas.create_image(400, 263, image=card_front)
language_label = canvas.create_text(
    400, 150, text='Language', font=("Arial", 40, "italic"))
word_label = canvas.create_text(
    400, 263, text='Word', font=("Arial", 60, "bold"))
timer_label = canvas.create_text(
    400, 400, text='5', font=("Arial", 40, "italic"))
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
