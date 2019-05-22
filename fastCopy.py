from tkinter import filedialog
from tkinter import *
import threadedCopy as tc

# Globals
DEFAULT_FILE_PATH = r"C:\Users\m0pxnn\Documents\Python"
WINDOW_TITLE = "Fast Copy (Brought to you by @SpanielMaximus)"
HEADING = "Multithreaded copy"

########################################################################################
# FastCopy class
########################################################################################
class FastCopy:
    def __init__(self, root):

        ##############################################################
        # Create a frame
        ##############################################################
        frame = Frame(root, padx=5, pady=5)
        frame.grid()

        ##############################################################
        # Heading text
        ##############################################################
        self.lblHeading = Label(frame, text=HEADING, padx=5, pady=5, fg="Blue", font='Verdana 15 bold underline')
        self.lblHeading.grid(columnspan=3)

        ##############################################################
        # Source
        ##############################################################
        self.lblSource = Label(frame, text="Source path")
        self.lblSource.grid(row=2, column=0, sticky=E)

        self.inpSource = Entry(frame, width=100)
        self.inpSource.insert(0, "")
        self.inpSource.grid(row=2, column=1)

        self.btnSource = Button(frame, text="Source", width=10, command=lambda: self.LaunchDirBrowser(self.inpSource, "Source"))
        self.btnSource.grid(row=2, column=3, pady=2)

        ##############################################################
        # Destination
        ##############################################################
        self.lblDest = Label(frame, text="Destination path")
        self.lblDest.grid(row=3, column=0, sticky=E)

        self.inpDest = Entry(frame, width=100)
        self.inpDest.insert(0, "")
        self.inpDest.grid(row=3, column=1)

        self.btnDest = Button(frame, text="Destination", width=10, command=lambda: self.LaunchDirBrowser(self.inpDest, "Destination"))
        self.btnDest.grid(row=3, column=3, pady=2)

        ##############################################################
        # Copy button
        ##############################################################
        self.btnCopy = Button(frame, text="Start Copy", padx=2, width=10, command=self.DoCopy)
        self.btnCopy.grid(row=5, column=3, pady=2)

        ##############################################################
        # Quit button
        ##############################################################
        self.btnCopy = Button(frame, text="Close", width=10, command=root.quit)
        self.btnCopy.grid(row=6, column=3, pady=2)

        ##############################################################
        # Status bar
        ##############################################################
        self.lblStatusBar = Label(root, text="Welcome to fast copy", width=100, bd=2, relief=SUNKEN)
        self.lblStatusBar.grid(row=6, columnspan=4, pady=1)

    ##############################################################
    # Launch folder browser
    ##############################################################
    def LaunchDirBrowser(self, entry, id):
        dirName = filedialog.askdirectory(initialdir=DEFAULT_FILE_PATH, title="Select folder")
        entry.delete(0, 'end')
        entry.insert(0, dirName)
        self.WriteToStatusBar("{} path updated".format(id))

    ##############################################################
    # Copy
    ##############################################################
    def DoCopy(self):
        if (self.inpSource.get() == "" or self.inpDest.get() == ""):
            self.WriteToStatusBar("Cannot copy. Source/Destination not specified")
        else:
            self.WriteToStatusBar("Beginning to copy...")
            tc.CopySourceToDest(self.inpSource.get(), self.inpDest.get())

    ##############################################################
    # API to write status
    ##############################################################
    def WriteToStatusBar(self, msg):
        self.lblStatusBar['text'] = msg

########################################################################################
# Create main window
########################################################################################
root = Tk()
root.title(WINDOW_TITLE)
fastCopy = FastCopy(root)
root.mainloop()