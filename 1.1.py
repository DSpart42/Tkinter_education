from tkinter import *

window = Tk()


form = Frame(relief = SUNKEN ,borderwidth = 3)
form.pack()

labels = [
    "Login:",
    "Password"
]
for idx, text in enumerate(labels):
    label = Label(master= form, text = text)
    entry = Entry(master= form, width = 30)

    label.grid(row = idx, column =0)
    entry.grid(row = idx, column =1)

window.mainloop()