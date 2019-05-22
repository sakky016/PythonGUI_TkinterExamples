from tkinter import *

root = Tk()

icon = PhotoImage(file="mario.png")
lbl = Label(root, text="Welcome", image=icon)
lbl.pack()

root.mainloop()