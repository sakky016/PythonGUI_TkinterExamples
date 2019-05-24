from tkinter import *

master = Tk()


def callback(number):
    print(number)


def make_callback(number):
    return (lambda: callback(number))


for i in range(0, 10):
    b = Button(master, text=str(i), command=make_callback(i))
    b.pack()

mainloop()