from tkinter import filedialog
from tkinter import *

# Globals
DEFAULT_FILE_PATH = r"C:\Users\m0pxnn\Documents\Python"


##############################################################
# Spawn threads to copy from source to destination
##############################################################
def CopySourceToDest(src, dst):
    print("Source       : ", src)
    print("Destination  : ", dst)
    # TODO

########################################################################################
# FastCopy class
########################################################################################
class FastCopy:
    def __init__(self, root):
        # Heading
        self.lblHeading = Label(root, text="Multithreaded copy", padx=5, pady=5)
        self.lblHeading.grid(row=0)

        ##############################################################
        # Source
        ##############################################################
        self.lblSource = Label(root, text="Source path", anchor=E)
        self.lblSource.grid(row=2, column=0)

        self.inpSource = Entry(root, width=100)
        self.inpSource.insert(0, "")
        self.inpSource.grid(row=2, column=1)

        #self.btnSource = Button(root, text="Source", padx=2, pady=2, command=self.LaunchDirBrowserSource)
        self.btnSource = Button(root, text="Source", padx=2, pady=2, command=lambda: self.LaunchDirBrowser(self.inpSource, "Source"))

        self.btnSource.grid(row=2, column=2)

        ##############################################################
        # Destination
        ##############################################################
        self.lblDest = Label(root, text="Destination path", anchor=E)
        self.lblDest.grid(row=3, column=0)

        self.inpDest = Entry(root, width=100)
        self.inpDest.insert(0, "")
        self.inpDest.grid(row=3, column=1)

        self.btnDest = Button(root, text="Destination", padx=2, pady=2, command=lambda: self.LaunchDirBrowser(self.inpDest, "Destination"))
        #self.btnDest.bind("<Button-1>", self.LaunchDirBrowserSourceDest)
        self.btnDest.grid(row=3, column=2)

        ##############################################################
        # Copy button
        ##############################################################
        self.btnCopy = Button(root, text="Start Copy", padx=2, pady=2)
        self.btnCopy.bind("<Button-1>", self.DoCopy)
        self.btnCopy.grid(row=4, column=2)

        ##############################################################
        # Status bar
        ##############################################################
        self.lblStatusBar = Label(root, text="Welcome to fast copy", width=100, padx=5, pady=5, bd=2, relief=SUNKEN)
        self.lblStatusBar.grid(row=6, columnspan=5)

    ##############################################################
    # Launch folder browser
    ##############################################################
    def LaunchDirBrowser(self, entry, id):
        dirName = filedialog.askdirectory(initialdir=DEFAULT_FILE_PATH, title="Select folder")
        entry.delete(0, 'end')
        entry.insert(0, dirName)
        self.WriteToStatusBar("Setting {} dir".format(id))

    ##############################################################
    # Copy
    ##############################################################
    def DoCopy(self, event):
        if (self.inpSource.get() == "" or self.inpDest.get() == ""):
            self.WriteToStatusBar("Cannot copy. Source/Destination not specified")
        else:
            self.WriteToStatusBar("Beginning to copy...")
            CopySourceToDest(self.inpSource.get(), self.inpDest.get())

    ##############################################################
    # API to write status
    ##############################################################
    def WriteToStatusBar(self, msg):
        self.lblStatusBar['text'] = msg

########################################################################################
# Create main window
########################################################################################
root = Tk()
root.title("Fast Copy")
fastCopy = FastCopy(root)
root.mainloop()