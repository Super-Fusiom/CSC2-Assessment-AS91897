from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


#Create the window
class Window:
    # quit the app
    def quitf(self):
        exit()
    # Collects the entries and placing them into the Customer Class
    # It checks for errors as well through a while loop
    def updatef(self):
        while True:
            if self.rootcount < 0:
                self.root2.protocol("WM_DELETE_WINDOW", self.result_close) 
            try: 
                if len(self.nametxt.get()) != 0:
                    str(self.nametxt.get())
                    customer.name = self.nametxt.get()
                else:
                    messagebox.showerror('error', 'Name field is blank')
                    break
            except ValueError:
                messagebox.showerror("error", "Name is not a number")
                break
            try:
                if len(self.receipttxt.get()) != 0:
                    int(self.receipttxt.get())
                    customer.receipt = self.receipttxt.get()
                else:
                    messagebox.showerror('error', 'Receipt field is blank')
            except ValueError:
                messagebox.showerror("error", "receipt number has no letters")
                break
            try:
                if len(self.itemtxt.get()) != 0: 
                    int(self.itemtxt.get())
                    messagebox.showerror('error', "item doesn't have numbers")
                    
                    break
                else:
                    messagebox.showerror('error', 'Item field is blank')
                    break
            except ValueError:
                customer.item = self.itemtxt.get()
            try:
                if len(self.quantitytxt.get()) != 0:
                    int(self.quantitytxt.get())
                    if self.quantitytxt.get() >= 1 and self.quantitytxt.get() <= 500:
                        customer.quantity = self.quantitytxt.get()
                    else:
                        messagebox.showerror('error', 'quantity has to be between 1 and 500')
                else:
                    messagebox.showerror('error' , 'Quantity field is blank')
                    break
            except ValueError:
                messagebox.showerror('error', "quantity doesn't have letters")
                break
            con = sqlite3.connect('save/save.db')
            cursorObj = con.cursor()
            try: 
                customer.row += 1
                cursorObj.execute("INSERT INTO customers (id, name, receipt, item, quantity) VALUES(?, ?, ?, ?, ?)", [customer.row, customer.name, customer.receipt, customer.item, customer.quantity])
            except sqlite3.OperationalError:
                messagebox.showerror("error", "whoops something happend in our end.")
            finally:
                con.commit()
                con.close()
                self.printf()
# Create the second window with the customer list.
    def printf(self):
        while self.rootcount <= 1:    
            self.root2 = Tk()
            self.rows = 1
            self.root2.title('results')
            self.rootcount += 1
            Label(self.root2, text="Row").grid(column=0, row=0, padx=20)
            Label(self.root2, text="Name").grid(column=1, row=0, padx=20)
            Label(self.root2, text="Receipt").grid(column=2, row=0, padx=20)
            Label(self.root2, text="Item").grid(column=3, row=0, padx=20)
            Label(self.root2, text="Quantity").grid(column=4, row=0, padx=20)
            self.root2.protocol("WM_DELETE_WINDOW", self.result_close)         
        #Database stuff
        def database():
            con = sqlite3.connect('save/save.db')
            cursorObj = con.cursor()

            cursorObj.execute("SELECT *, oid FROM customers")
            records = cursorObj.fetchall()

            for record in records:
                rid = ttk.Label(self.root2, text=str(record[0]))
                rid.grid(row=self.rows, column=0, padx=20)
                rname = ttk.Label(self.root2, text=str(record[1]))
                rname.grid(row=self.rows, column=1, padx=20)
                rreceipt = ttk.Label(self.root2, text=str(record[2]))
                rreceipt.grid(row=self.rows, column=2, padx=20)
                ritem = ttk.Label(self.root2, text=str(record[3]))
                ritem.grid(row=self.rows, column=3, padx=20)
                rquantity = ttk.Label(self.root2, text=str(record[4]))
                rquantity.grid(row=self.rows, column=4, padx=20)
                self.rows += 1
            con.commit()
            con.close()
        database()
    #when the second window is closed
    def result_close(self):
        self.rows = 1
        self.rootcount = 1
        self.root2.destroy()
    def delete_row(self):
        con = sqlite3.connect('save/save.db')
        c = con.cursor()

        c.execute("DELETE FROM customers WHERE oid=" + self.deletetxt.get())

        con.commit()
        con.close()
    # The constructor/ __init__
    def __init__(self):
        self.root = Tk()
        self.root.title('Party Hire')
        # Buttons
        def buttons():
            self.quitbtn = ttk.Button(self.root, text='Quit', command=self.quitf).grid(column=2, row=1, padx=5)
            self.updatebtn = ttk.Button(self.root, text='Update', command=self.updatef).grid(column=0, row=1, padx=5)
            self.printbtn = ttk.Button(self.root, text='Print', command=self.printf).grid(column=1, row=1, padx=5)
            self.deletebtn = ttk.Button(self.root, text='Delete Row', command=self.delete_row).grid(column=2, row=6)
        def image():
            #Image is here
            logoimg = PhotoImage(file="image/hire-logo.png")
            logo = ttk.Label(self.root, image=logoimg)
            logo.image = logoimg
            logo.grid(column=0 ,row=0, columnspan=2)
        self.rows = 1
        #root count reset
        self.rootcount = 1
        #Labels
        def labels():
            self.namelb = ttk.Label(self.root, text="Name").grid(column=0, row=2)
            self.receiptlb = ttk.Label(self.root, text="Receipt Number").grid(column=0, row=3)
            self.itemlb = ttk.Label(self.root, text="Item").grid(column=0, row=4)
            self.quantitylb = ttk.Label(self.root, text="Quantity").grid(column=0, row=5)
        # Text Box
        self.nametxt = ttk.Entry(self.root, text="")
        self.nametxt.grid(column=1, row=2)
        self.receipttxt = ttk.Entry(self.root, text="")
        self.receipttxt.grid(column=1, row=3)
        self.itemtxt = ttk.Entry(self.root, text="")
        self.itemtxt.grid(column=1, row=4)
        self.quantitytxt = ttk.Entry(self.root, text="")
        self.quantitytxt.grid(column=1, row=5)
        self.deletetxt = ttk.Entry(self.root, text="")
        self.deletetxt.grid(row=6, column=0, columnspan=2)
        buttons()
        labels()
        image()
class Customer:
    def __init__(self):
        self.row = 1
        self.name = ""
        self.receipt = ""
        self.item = ""
        self.quantity = ""

window = Window()
customer = Customer()

window.root.mainloop()