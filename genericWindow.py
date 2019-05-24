from tkinter import *

inputFieldNames = ["First Name", "Last Name", "Address", "City", "State", "Pincode"]
buttonNames = ["Submit", "Reset", "Close"]
INPUT_FIELD_WIDTH = 20
STATUS_BAR_WIDTH = 40

############################################################################
# Application class
############################################################################
class Application:
    # Widget variable dictionary
    widget = {}

    # List of Widgets
    label = []
    entry = []
    button = []

    # Constructor
    def __init__(self, root):
        rowIndex = 0
        columnIndex = 0

        # Create label and entry field
        for inputFieldName in inputFieldNames:
            # Label
            columnIndex = 0
            #print("Adding label at ({},{})".format(rowIndex,columnIndex))
            self.label.append(Label(root, text=inputFieldName, padx=2, pady=2, anchor=E))
            self.label[rowIndex].grid(row=rowIndex, column=0)

            # Entry field
            columnIndex = 1
            #print("Adding entry field at ({},{})".format(rowIndex, columnIndex))
            self.widget[inputFieldName] = StringVar()
            self.widget[inputFieldName].trace("w", self.callbackEntryField)
            self.entry.append(Entry(root, text="", width=INPUT_FIELD_WIDTH, textvariable=self.widget[inputFieldName]))
            self.entry[rowIndex].grid(row=rowIndex, column=1)

            rowIndex = rowIndex + 1

        # Create buttons
        columnIndex = 0
        for buttonName in buttonNames:
            #print("Adding button at ({},{})".format(rowIndex,columnIndex))
            self.widget[buttonName] = StringVar()
            print("Registering callback for [{}]".format(buttonName))
            self.button.append(Button(root, text=buttonName, padx=2, pady=2, command=self.makeCallback(buttonName)))
            self.button[len(self.button) - 1].grid(row=rowIndex, column=columnIndex)
            columnIndex = columnIndex + 1

        # Create status bar
        columnIndex = 0
        rowIndex = rowIndex + 1
        self.lblStatusBarTitle = Label(root, text="Status: ")
        self.lblStatusBarTitle.grid(row=rowIndex, column=columnIndex)

        columnIndex = columnIndex + 1
        self.lblStatusBar = Label(root, text="Welcome", width=STATUS_BAR_WIDTH, bd=1, relief=SUNKEN)
        self.lblStatusBar.grid(row=rowIndex, column=columnIndex)

        self.DisplayWidgets()

    # Function to set status bar message
    def SetStatusBarMsg(self, msg):
        self.lblStatusBar.config(text=msg)

    # Directly using the body of this function at the time of registering callback
    # in button doesn't work! Don't know why. It keeps on registering only the last
    # registered buttonName.
    def makeCallback(self, buttonName):
        return lambda: self.callbackFunc(buttonName)

    def makeEntryFieldCallback(self, *args):
        return lambda: self.callbackEntryField()

    # Called when entry field is updated
    def callbackEntryField(self, *args):
        self.SetStatusBarMsg("[{}] updated".format(args[0]))

    # callback function for button
    def callbackFunc(self, buttonName):
        #print("{} button was pressed".format(buttonName))
        self.SetStatusBarMsg("{} button was pressed".format(buttonName))

        if (buttonName == "Submit"):
            self.SetStatusBarMsg("Thank you for submitting details".format(buttonName))
        elif (buttonName == "Reset"):
            for e in self.entry:
                print("Clearing field [{}]".format(e.get()))
                e.delete(0, 'end')
            self.SetStatusBarMsg("Clearing input fields".format(buttonName))
        elif (buttonName == "Close"):
                root.quit()

    # Display what all widgets have been registered in this application
    def DisplayWidgets(self):
        print("Available Widgets:")
        index = 0
        for widget in self.widget:
            print("{}) {}".format(index, widget))
            index = index + 1

#####################################################################################
# Main
#####################################################################################
root = Tk()
root.title("Generic Window Example")

app = Application(root)
root.mainloop()