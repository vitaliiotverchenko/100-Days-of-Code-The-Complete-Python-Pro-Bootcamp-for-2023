import tkinter as tk
import random as rd
import string
import pyperclip
from tkinter import messagebox


STANDARD_EMAIL = 'vitaliiotverchenko@gmail.com'
STANDARD_FONT = ("Arial", 18)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, tk.END)
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    password_letters = [rd.choice(letters) for _ in range(rd.randint(8, 10))]
    password_symbols = [rd.choice(symbols) for _ in range(rd.randint(2, 4))]
    password_numbers = [rd.choice(numbers) for _ in range(rd.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    rd.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(
            title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(
        title=website, message=f"These are details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("Day_29_Password_generator\data.txt", 'a+', encoding='utf-8') as data:
            data.write(
                f"{website} | {email} | {password}\n")
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password manager")
window.minsize(width=600, height=420)
window.config(padx=50, pady=50, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = tk.PhotoImage(file="Day_29_Password_generator/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0, sticky='e')


# labels
website_label = tk.Label(text="Website:", bg="white",
                         font=STANDARD_FONT)
website_label.grid(column=0, row=1)
website_label.config(padx=10, pady=10)

email_username_label = tk.Label(
    text="Email/Username:", bg="white", font=STANDARD_FONT)
email_username_label.grid(column=0, row=2)
email_username_label.config(padx=10, pady=10)

password_label = tk.Label(text="Password:", bg="white",
                          font=STANDARD_FONT)
password_label.grid(column=0, row=3)
password_label.config(padx=10, pady=10)

# Entry forms
website_entry = tk.Entry(width=34, font=STANDARD_FONT)
website_entry.grid(column=1, row=1,  columnspan=2, sticky="w")
website_entry.focus()

email_username_entry = tk.Entry(width=34, font=STANDARD_FONT)
email_username_entry.insert(0, string=STANDARD_EMAIL)
email_username_entry.grid(column=1, row=2,  columnspan=2, sticky="w")

password_entry = tk.Entry(width=20, font=STANDARD_FONT)
password_entry.grid(column=1, row=3, sticky="w")


# Buttons
generate_password_button = tk.Button(
    text="Generate Password", font=STANDARD_FONT, command=generate_password)
generate_password_button.grid(column=2, row=3)


add_button = tk.Button(text="Add", width=36, font=(
    STANDARD_FONT), command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w',
                pady=15)


window.mainloop()
