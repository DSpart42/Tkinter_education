from tkinter import *
from random import randint

def gen():
    lbl_value["text"] = f"{randint(1,6)}"

window = Tk()
window.rowconfigure([0,1], minsize = 50, weight = 1)
window.columnconfigure(0, minsize = 150, weight = 1)

button = Button(
    master = window,
    text = "click",
    command = gen
)

lbl_value = Label(
    master = window,
    text = "0"
)

button.grid(row=0, column=0, sticky="nsew")
lbl_value.grid(row=1, column=0, sticky="nsew")

window.mainloop()