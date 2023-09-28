import tkinter as tk
import math
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(clock, text="00:00")
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    reps = 0
    return
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    check_mark_label.config(
        text=f"{CHECK_MARK * (reps // 2)}", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # If it's the 1st, 3th, 5th, 7th rep:
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    # If it's the 2nd, 4th, 6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(clock, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=200, height=233)
window.config(padx=100, pady=50, bg=YELLOW)

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
    FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

# Initialized the label "Check mark"
check_mark_label = tk.Label(
    text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_mark_label.grid(column=1, row=3)
check_mark_label.config(padx=10, pady=10)


window.mainloop()
