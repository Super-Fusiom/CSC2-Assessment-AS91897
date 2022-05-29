from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title('Party Hire')
class Window:
    def __init__(self, master):
        #rootcount is used to check if the second window is open to deny extra instances
        global rootcount
        myFrame = ttk.Frame(master).grid()
        # Buttons
        self.quitbtn = ttk.Button(myFrame, text='Quit', command=self.quitf).grid(column=2, row=1, padx=5)
        self.updatebtn = ttk.Button(myFrame, text='Update', command=self.window2).grid(column=0, row=1, padx=5)
        self.printbtn = ttk.Button(myFrame, text='Print', command=self.printf).grid(column=1, row=1, padx=5)
        rootcount = 1

        #Labels
        self.namelb = ttk.Label(myFrame, text="Name").grid(column=0, row=2)
        self.receiptlb = ttk.Label(myFrame, text="Receipt Number").grid(column=0, row=3)
        self.itemlb = ttk.Label(myFrame, text="Item").grid(column=0, row=4)
        self.quantitylb = ttk.Label(myFrame, text="Quantity").grid(column=0, row=5)
        # Text Box
        self.nametxt = ttk.Entry(myFrame).grid(column=1, row=2)
        self.receipttxt = ttk.Entry(myFrame).grid(column=1, row=3)
        self.itemtxt = ttk.Entry(myFrame).grid(column=1, row=4)
        self.quantitytxt = ttk.Entry(myFrame).grid(column=1, row=5) 
    # quit the app
    def quitf(self):
        exit()
    
    def printf(self):
        self.window2()

    def window2(self):
        global rootcount, root2
        while rootcount <= 1:
            root2 = Tk()
            root2.title('results')
            frame2 = ttk.Frame(root2)
            rootcount += 1
            root2.protocol("WM_DELETE_WINDOW", self.result_close)
    def result_close(self):
        global rootcount, root2
        rootcount = 1
        root2.destroy()


window = Window(root)

root.mainloop()