import tkinter as tk
import random as rd
import string
import pyperclip
import json
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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(
            title="Oops", message="Please make sure you haven't left any fields empty.")
        return
    try:
        with open("Day_29_Password_generator\data.json", 'r') as data:
            # Try to load existing data from the file
            data_dict = json.load(data)
            data_dict.update(new_data)
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open("Day_29_Password_generator/data.json", 'w') as data:
            # Save the new data
            json.dump(new_data, data, indent=4)
    else:
        # Open the file in write mode to save the updated data
        with open("Day_29_Password_generator/data.json", 'w') as data:
            # Save the updated data
            json.dump(data_dict, data, indent=4)
    finally:
        # Clear the entry fields and set focus to website_entry
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()


def search_password():
    website = website_entry.get()
    try:
        with open("Day_29_Password_generator/data.json", 'r') as data:
            data_dict = json.load(data)
            if website in data_dict:
                email = data_dict[website]["email"]
                password = data_dict[website]["password"]
                messagebox.showinfo(
                    title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(
                    title="Oops", message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showerror(
            title="Oops", message="No data file found.")
    finally:
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()
        return
    # ---------------------------- SAVE PASSWORD ------------------------------- #
    # ---------------------------- UI SETUP ------------------------------- #
    # ---------------------------- PASSWORD GENERATOR -------------------------------


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
website_entry = tk.Entry(width=20, font=STANDARD_FONT)
website_entry.grid(column=1, row=1,  columnspan=2, sticky="w")
website_entry.focus()

email_username_entry = tk.Entry(width=34, font=STANDARD_FONT)
email_username_entry.insert(0, string=STANDARD_EMAIL)
email_username_entry.grid(column=1, row=2,  columnspan=2, sticky="w")

password_entry = tk.Entry(width=20, font=STANDARD_FONT)
password_entry.grid(column=1, row=3, sticky="w")


# BUTTONS
search_button = tk.Button(
    text="Search", width=16, font=STANDARD_FONT, command=search_password)
search_button.grid(column=2, row=1)

generate_password_button = tk.Button(
    text="Generate Password", font=STANDARD_FONT, command=generate_password)
generate_password_button.grid(column=2, row=3)


add_button = tk.Button(text="Add", width=36, font=(
    STANDARD_FONT), command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w',
                pady=15)


window.mainloop()
