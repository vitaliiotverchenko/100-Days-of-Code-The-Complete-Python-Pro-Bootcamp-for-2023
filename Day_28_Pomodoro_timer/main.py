import tkinter as tk
import time, math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 1st rep, start the timer for 25 minutes
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    
    count_down(5 * 60)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(clock, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)




# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=200, height=233)
window.config(padx=100, pady=50, bg=YELLOW)

# 1000 mili_sec = 1 sec
# mili_sec = 1000
# window.after()


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="Day_28_Pomodoro_timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
clock = canvas.create_text(100, 130, text="00:00",
                           fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Initialized the label "Timer"
timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN,
                       font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)
timer_label.config(padx=10, pady=10)

# Initialized the button "Start"
start_button = tk.Button(text="Start", font=(
    FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Initialized the button "Reset"
reset_button = tk.Button(text="Reset", font=(
    FONT_NAME, 15, "bold"), highlightthickness=0)
reset_button.grid(column=3, row=2)

# Initialized the label "Check mark"
check_mark_label = tk.Label(
    text=CHECK_MARK, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_mark_label.grid(column=1, row=3)
check_mark_label.config(padx=10, pady=10)


window.mainloop()
