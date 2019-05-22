from tkinter import *

def Func():
    print("Called from toolbar")

root = Tk()

lbl = Label(root, text="Canvas:")
lbl.pack(anchor=W)

canvas = Canvas(root, width=200, height=200, bd= 1, relief=SUNKEN)
canvas.pack()

blackLine = canvas.create_line(10,10, 200, 200)
redLine = canvas.create_line(10,200, 200, 10, fill="red")

greenBox = canvas.create_rectangle(50,50, 100,100, fill="green")

blueCircle = canvas.create_oval(60, 60, 80, 80, fill="blue")

# Deleting a canvas element
canvas.delete(redLine)
#canvas.delete(ALL)  # Delete entire canvas



root.mainloop()