from tkinter import *
from tkinter import messagebox

#Create the window
class Window:
    # quit the app
    def quitf(self):
        exit()
    # Collects the entries and placing them into the Customer Class
    def updatef(self):
        customer.name = self.nametxt.get()
        customer.receipt = self.receipttxt.get()
        customer.item = self.itemtxt.get()
        customer.quantity = self.quantitytxt.get()
        print(customer.name)
        self.printf()
# Create the second window with the customer list.
    def printf(self):
        while self.rootcount <= 1:
            self.root2 = Tk()
            self.root2.title('results')
            self.rootcount += 1
            self.root2.protocol("WM_DELETE_WINDOW", self.result_close)
        self.rname = Label(self.root2, text=customer.name).grid(row=self.rows, column=0, padx=20)
        self.rreceipt = Label(self.root2, text=customer.receipt).grid(row=self.rows, column=1, padx=20)
        self.ritem = Label(self.root2, text=customer.item).grid(row=self.rows, column=2, padx=20)
        self.rquantity = Label(self.root2, text=customer.quantity).grid(row=self.rows, column=3, padx=20)
        self.rows += 1
    #when the second window is closed
    def result_close(self):
        self.rootcount = 1
        self.root2.destroy()
    # The constructor/ __init__
    def __init__(self):
        self.root = Tk()
        self.root.title('Party Hire')
        # Buttons
        self.quitbtn = Button(self.root, text='Quit', command=self.quitf).grid(column=2, row=1, padx=5)
        self.updatebtn = Button(self.root, text='Update', command=self.updatef).grid(column=0, row=1, padx=5)
        self.printbtn = Button(self.root, text='Print', command=self.printf).grid(column=1, row=1, padx=5)
        self.rootcount = 1
        #Labels
        self.namelb = Label(self.root, text="Name").grid(column=0, row=2)
        self.receiptlb = Label(self.root, text="Receipt Number").grid(column=0, row=3)
        self.itemlb = Label(self.root, text="Item").grid(column=0, row=4)
        self.quantitylb = Label(self.root, text="Quantity").grid(column=0, row=5)
        # Text Box
        self.nametxt = Entry(self.root, text="")
        self.nametxt.grid(column=1, row=2)
        self.receipttxt = Entry(self.root, text="")
        self.receipttxt.grid(column=1, row=3)
        self.itemtxt = Entry(self.root, text="")
        self.itemtxt.grid(column=1, row=4)
        self.quantitytxt = Entry(self.root, text="")
        self.quantitytxt.grid(column=1, row=5)
        self.rows = 0
class Customer:
    def __init__(self):
        self.name = ""
        self.receipt = ""
        self.item = ""
        self.quantity = ""

window = Window()
customer = Customer()

window.root.mainloop()