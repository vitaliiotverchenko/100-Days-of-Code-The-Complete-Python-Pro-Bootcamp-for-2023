from tkinter import *

# Initialized the window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Initialized the entry form
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)


# Initialized the label "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

# Initialized the label "is equal to"
label = Label(text="is equal to")
label.grid(column=0, row=2)
# label.config(padx=10, pady=10)

# Initialized the label "result of calculating"
km_label = Label(text="0")
km_label.grid(column=1, row=2)
# label.config(padx=10, pady=20)

# Initialized the label "km"
label = Label(text="Km")
label.grid(column=2, row=2)
# label.config(padx=10, pady=20)


def miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609, 2)
    km_label.config(text=f"{km}")

# Initialized the button "Calculate"
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)





window.mainloop()
