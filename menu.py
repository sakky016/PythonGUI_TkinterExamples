from tkinter import *
import tkinter.messagebox

def Func():
    print("Called from menu")
    tkinter.messagebox.showinfo("Menu bar", "A button was pressed from the Menubar")

def ButtonFunc():
    print("Button function called")
    tkinter.messagebox.showinfo("Toolbar button", "A button was pressed from the toolbar")

# Function called when Quit is pressed
def QuitWindow():
    answer = tkinter.messagebox.askquestion("Quit", "Are you sure you want to quit?")
    if (answer == "yes"):
        root.quit()
    else:
        print("Ignoring exit button")


# Create main window
root = Tk()
root.title("Main window")

# *** Main Menu ***
# menu bar
menuBar = Menu(root)
root.config(menu=menuBar)

# Menu item-1: File
subMenuFile = Menu(menuBar)
menuBar.add_cascade(label="File", menu=subMenuFile)
subMenuFile.add_command(label="New", command=Func)
subMenuFile.add_command(label="Save", command=Func)
subMenuFile.add_separator()
subMenuFile.add_command(label="Exit", command=QuitWindow)

# Menu item-2: Edit
subMenuEdit = Menu(menuBar)
menuBar.add_cascade(label="Edit", menu=subMenuEdit)
subMenuEdit.add_command(label="Undo", command=Func)
subMenuEdit.add_command(label="Redo", command=Func)
subMenuEdit.add_command(label="Copy", command=Func)
subMenuEdit.add_separator()
subMenuEdit.add_command(label="Cut", command=Func)
subMenuEdit.add_command(label="Paste", command=Func)

# *** Toolbar ***
toolbar = Frame(root, bg="white")

btn1 = Button(toolbar, text="Button1", command=ButtonFunc)
btn1.pack(side=LEFT, padx=2, pady=2)

btn2 = Button(toolbar, text="Button2", command=ButtonFunc)
btn2.pack(side=LEFT, padx=2, pady=2)

btn3 = Button(toolbar, text="Button3", command=ButtonFunc)
btn3.pack(side=LEFT, padx=1, pady=1)

toolbar.pack(side=TOP, fill=X)

# *** Status Bar ***
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



# Main window loop
root.mainloop()