import tkinter


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")

my_label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Input 
input = tkinter.Entry(width=10)
input.pack()




window.mainloop()
