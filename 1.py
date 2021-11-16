from tkinter import *

window = Tk()
window.geometry("400x300")

border_effects = {
    "flat": FLAT,
    "sunken": SUNKEN,
    "raised": RAISED,
    "groove": GROOVE,
    "ridge": RIDGE,
}

frame_a = Frame()
frame_b = Frame()

label_a = Label(
    master = frame_a,
    text = "Name:",
    fg = "purple"
)
label_a.pack()

entry_a = Entry(master = frame_a)
entry_a.pack()

label_b = Label(
    master = frame_b,
    text = "Surname:",
    fg = "purple",
    relief = RAISED
)
label_b.pack()

entry_b = Entry(master = frame_b)
entry_b.pack()

frame_b.pack(side = LEFT)
frame_a.pack(side = LEFT)

window.mainloop()