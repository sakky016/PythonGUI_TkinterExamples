from tkinter import *

root = Tk()
root.title("Variable Widget Association Demo")

bgColor = "#EDEDED"

# Widget Variable dictionary
Values = {}

def Submit():
    print("\nThe user clicked the 'Submit' button.")

    # Without using variable
    print("Text box content: ", inp.get())

    for key, value in Values.items():
        #print(key, value)
        if key == 'BoxSync':
            if (value.get() == 1):
                print("User ENABLED BoxSync")
            else:
                print("User DISABLED BoxSync")

        if key == 'CrashPlan':
            if (value.get() == 1):
                print("User ENABLED CrashPlan")
            else:
                print("User DISABLED CrashPlan")

        if key == 'inp':
            print("Entry value: ", value.get())

# Event callbacks
def cb_1(*args):
    print ("BoxSync was updated to [{}]".format(Values['BoxSync'].get()))

def cb_2(*args):
    print ("CrashPlan was updated [{}]".format(Values['CrashPlan'].get()))

def cb_3(*args):
    print ("Text field was updated to [{}]".format(Values['inp'].get()))

Values['BoxSync'] = BooleanVar()
Values['BoxSync'].trace("w", cb_1)
ck1 = Checkbutton(root, text = "Box Sync", font=("Helvetica Neue", 14), variable = Values['BoxSync'], bg = bgColor).grid(row = 1, column = 2, sticky = 'w')

Values['CrashPlan'] = BooleanVar()
Values['CrashPlan'].trace("w", cb_2)
ck2 = Checkbutton(root, text = "CrashPlan", font=("Helvetica Neue", 14), variable = Values['CrashPlan'], bg = bgColor).grid(row = 1, column = 3, columnspan = 2, padx = (0, 10), sticky = 'w')

Values['inp'] = StringVar()
Values['inp'].trace("w", cb_3)
inp = Entry(root, textvariable=Values['inp'])
inp.grid(row=2)

btnSubmit = Button(root, text="Submit", command=Submit)
btnSubmit.grid(row=3, column=0)

root.mainloop()