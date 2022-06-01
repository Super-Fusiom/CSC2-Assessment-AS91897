from tkinter import *
from tkinter import messagebox
import sqlite3

#Create the window
class Window:
    # quit the app
    def quitf(self):
        exit()
    # Collects the entries and placing them into the Customer Class
    # It checks for errors as well
    def updatef(self):
        customer.name = self.nametxt.get()
        customer.receipt = self.receipttxt.get()
        customer.item = self.itemtxt.get()
        customer.quantity = self.quantitytxt.get()
        con = sqlite3.connect('save/save.db')
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE customers(id integer PRIMARY KEY, name text, receipt real, item text, quanitity integer")
        cursorObj.execute("INSERT INTO customers (name, receipt, item, quantity) VALUES(?, ?, ?, ?, ?",customer.name, customer.receipt, customer.item, customer.quantity)
        con.commit()
        self.printf()
# Create the second window with the customer list.
    def printf(self):
        while True:
            if len(self.nametxt.get()) == 0:
                messagebox.showerror('No name', 'Please input a name')
                break
            try:
                str(self.nametxt.get())
                if len(self.receipttxt.get()) == 0:
                    messagebox.showerror('No receipt', 'Input receipt')
                    break
                try:
                    int(self.receipttxt.get())
                    if len(self.itemtxt.get()) == 0:
                        messagebox.showerror('Item', 'Insert an item')
                    try: 
                        str(self.itemtxt.get())
                        if len(self.quantitytxt.get()) == 0:
                            messagebox.showerror('Quantity', 'What is the quantity?')
                            break
                        try: 
                            int(self.quantitytxt.get())
                            if self.rootcount <= 1:
                                self.root2 = Tk()
                                self.root2.title('results')
                                self.rootcount += 1
                                Label(self.root2, text="Row").grid(column=0, row=0)
                                Label(self.root2, text="Name").grid(column=1, row=0)
                                Label(self.root2, text="Receipt").grid(column=2, row=0)
                                self.root2.protocol("WM_DELETE_WINDOW", self.result_close)
                                break
                            # Display the inputs
                            self.rname = Label(self.root2, text=customer.name).grid(row=self.rows, column=0, padx=20)
                            self.rreceipt = Label(self.root2, text=customer.receipt).grid(row=self.rows, column=1, padx=20)
                            self.ritem = Label(self.root2, text=customer.item).grid(row=self.rows, column=2, padx=20)
                            self.rquantity = Label(self.root2, text=customer.quantity).grid(row=self.rows, column=3, padx=20)
                            self.rows += 1
                        except ValueError:
                            messagebox.showerror('Quantity', 'Number only')
                            break
                    except ValueError:
                        messagebox.showerror('Item', 'Letters only')
                        break   
                except ValueError:
                    messagebox.showerror('Receipt', "Numbers only")
                    break
            except:
                messagebox.showerror('Numbers?', "Input letters in name")
                break
    #when the second window is closed
    def result_close(self):
        self.rows = 1
        self.rootcount = 1
        self.root2.destroy()
    def delete_row(self):
        print(5)
    # The constructor/ __init__
    def __init__(self):
        self.root = Tk()
        self.root.title('Party Hire')
        # Buttons
        def buttons():
            self.quitbtn = Button(self.root, text='Quit', command=self.quitf).grid(column=2, row=1, padx=5)
            self.updatebtn = Button(self.root, text='Update', command=self.updatef).grid(column=0, row=1, padx=5)
            self.printbtn = Button(self.root, text='Print', command=self.printf).grid(column=1, row=1, padx=5)
            self.deletebtn = Button(self.root, text='Delete Row', command=self.delete_row).grid(column=2, row=6)
        #root count reset
        self.rootcount = 1
        #Labels
        def labels():
            self.namelb = Label(self.root, text="Name").grid(column=0, row=2)
            self.receiptlb = Label(self.root, text="Receipt Number").grid(column=0, row=3)
            self.itemlb = Label(self.root, text="Item").grid(column=0, row=4)
            self.quantitylb = Label(self.root, text="Quantity").grid(column=0, row=5)
        # Text Box
        def entry():
            self.nametxt = Entry(self.root, text="")
            self.nametxt.grid(column=1, row=2)
            self.receipttxt = Entry(self.root, text="")
            self.receipttxt.grid(column=1, row=3)
            self.itemtxt = Entry(self.root, text="")
            self.itemtxt.grid(column=1, row=4)
            self.quantitytxt = Entry(self.root, text="")
            self.quantitytxt.grid(column=1, row=5)
            self.deletetxt = Entry(self.root, text="")
            self.deletetxt.grid(row=6, column=0, columnspan=2)
        buttons()
        labels()
        entry()
        self.rows = 1
class Customer:
    def __init__(self):
        self.name = ""
        self.receipt = ""
        self.item = ""
        self.quantity = ""

window = Window()
customer = Customer()

window.root.mainloop()