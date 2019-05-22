from tkinter import *

# Create tkinter
root = Tk()

#lb = Label(root, text="Here goes label")
#lb.pack()

#topFrame = Frame(root)
#topFrame.pack()

#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)

def SubmitButton(event):
    newWindow = Tk()
    #newWindow.mainloop()
    if (event == "<Button-1>"):
        print("Clicked!")
    elif (event == "<Enter>"):
        print("Mouse Over")



# Widgets
lbl1 = Label(root, text="Name")
lbl2 = Label(root, text="Password")

entry1 = Entry(root)
entry2 = Entry(root)

btn1 = Button(root, text="Click Me")
btn1.bind("<Button-1>", SubmitButton)
btn1.bind("<Enter>", SubmitButton)

btn2 = Button(root, text="Quit", command=root.quit)

chk1 = Checkbutton(root, text="Keep me logged in")

# Widget layout
lbl1.grid(row=0, column=0, sticky=E)
lbl2.grid(row=1, column=0, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
btn1.grid(row=2, column=0, columnspan=2)
btn2.grid(row=2, column=1)
chk1.grid(row=3)



# Main event loop
root.mainloop()