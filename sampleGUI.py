from tkinter import Tk, Label, Button, StringVar

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.greet_button.bind("<Enter>", self.mouseOverEnter)
        self.greet_button.bind("<Leave>", self.mouseOverLeave)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
        self.varHintLabel = StringVar()
        self.hintLabel = Label(master, textvariable=self.varHintLabel)
        self.hintLabel.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        
    def mouseOverEnter(self, event):
        self.varHintLabel.set("Click to greet") 

    def mouseOverLeave(self, event):
        self.varHintLabel.set("")         

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()