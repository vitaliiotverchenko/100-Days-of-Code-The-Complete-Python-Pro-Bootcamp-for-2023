import tkinter as tk
import random as rd
import string
import secrets

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# def generate_password():
#     password_entry.delete(0, tk.END)
#     letters = string.ascii_letters
#     numbers = string.digits
#     symbols = string.punctuation

    



# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password manager")
window.minsize(width=600, height=420)
window.config(padx=20, pady=20, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = tk.PhotoImage(file="Day_29_Password_generator/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0, sticky='w')


# labels
website_label = tk.Label(text="Website:", bg="white",
                         font=("Arial", 18, "bold"))
website_label.grid(column=0, row=1)
website_label.config(padx=10, pady=10)

email_username_label = tk.Label(
    text="Email/Username:", bg="white", font=("Arial", 18, "bold"))
email_username_label.grid(column=0, row=2)
email_username_label.config(padx=10, pady=10)

password_label = tk.Label(text="Password:", bg="white",
                          font=("Arial", 18, "bold"))
password_label.grid(column=0, row=3)
password_label.config(padx=10, pady=10)

# Entry forms
website_entry = tk.Entry(width=55)
website_entry.grid(column=1, row=1,  columnspan=2)

email_username_entry = tk.Entry(width=55)
email_username_entry.grid(column=1, row=2,  columnspan=2)

password_entry = tk.Entry(width=35)
password_entry.grid(column=1, row=3, sticky="w")


# Buttons
generate_password_button = tk.Button(
    text="Generate Password")
# TODO: Add functionality to the button ( command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')


window.mainloop()
