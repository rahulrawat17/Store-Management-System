from tkinter import *
import tkinter.messagebox
import sqlite3
conn = sqlite3.connect('store.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS inventory(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, stock INTEGER, cp INTEGER, sp INTEGER, totalcp INTEGER, totalsp INTEGER, assumed_profit INTEGER, vendor TEXT, vendor_phone INTEGER)')

sql11 = "SELECT * FROM INVENTORY WHERE id=?"
xx1 = 987654321
result = c.execute(sql11, (0, ))
for i in result:
    xx1 = i[0]
conn.commit()
if xx1 == 987654321:
    c.execute("INSERT INTO inventory(id, name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phone) VALUES(0,'test',0,0,0,0,0,0,'test',0)")

result = c.execute("SELECT MAX(id) FROM inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self,master,*args,**kwargs):

        self.master = master
        self.heading = Label(master, text ='>> Add to the Database <<',font =('arial 40 bold'), fg ='steelblue')
        self.heading.place(x=400,y=0)
        
        #labels for entries for the window
        self.id_l = Label(master, text ='Enter ID*', font =('arial 18 bold'))
        self.id_l.place(x=20,y=100)
        self.name_1 = Label(master, text ='Enter Product Name*', font =('arial 18 bold'))
        self.name_1.place(x=20,y=150)
        self.stock_l = Label(master, text ='Enter Stocks*', font =('arial 18 bold'))
        self.stock_l.place(x=20,y=200)
        self.cp_l = Label(master, text ='Enter Cost Price*', font =('arial 18 bold'))
        self.cp_l.place(x=20,y=250)
        self.sp_l = Label(master, text ='Enter Selling Price*', font =('arial 18 bold'))
        self.sp_l.place(x=20,y=300)
        self.vendor_l = Label(master, text ='Enter Vendor Name', font =('arial 18 bold'))
        self.vendor_l.place(x=20,y=350)
        self.vendor_phone_l = Label(master, text ='Enter Vendor Phone no.', font =('arial 18 bold'))
        self.vendor_phone_l.place(x=20,y=400)
        self.t_c = Label(master, text ='*input required', font =('arial 15'))
        self.t_c.place(x=20,y=470)
        
        self.logo = Label(master, text ='>> RS STORE <<', font =('arial 40 bold'), fg ='red')
        self.logo.place(x=850,y=580)


        #entries for the lables
        self.id_e = Entry(master, width= 25, font =('arial 18 bold'))
        self.id_e.place(x=320,y=100)
        self.id_e.insert(END, str(id + 1))
        self.name_e = Entry(master, width =25, font =('arial 18 bold'))
        self.name_e.place(x=320,y=150)
        self.name_e.focus()
        self.stock_e = Entry(master, width =25, font =('arial 18 bold'))
        self.stock_e.place(x=320,y=200)
        self.cp_e = Entry(master, width =25, font =('arial 18 bold'))
        self.cp_e.place(x=320,y=250)
        self.sp_e = Entry(master, width =25, font =('arial 18 bold'))
        self.sp_e.place(x=320,y=300)
        self.vendor_e = Entry(master, width =25, font =('arial 18 bold'))
        self.vendor_e.place(x=320,y=350)
        self.vendor_phone_e = Entry(master, width =25, font =('arial 18 bold'))
        self.vendor_phone_e.place(x=320,y=400)

        #button to add to the database
        self.btn_add = Button(master, text ='Add to the database', width =20, height =2, bg ='steelblue', fg ='white', command =self.get_items)
        self.btn_add.place(x=490,y=450)

        #button for clearing fields
        self.btn_clear = Button(master, text = 'Clear all fields', width =20, height =2, bg ='green', fg ='white', command =self.clear_all)
        self.btn_clear.place(x=300,y=450)

        #text box for the logs
        self.tbox = Text(master, width =50, height =16)
        self.tbox.place(x=720,y=100)

        self.tbox.insert(END, "ID has reached upto: " + str(id))
        

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        self.id_e.delete(0, END)

    def get_items(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()
        
        #dynamic entries
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo('error','empty input try again...')
        else:
            sql = "INSERT INTO inventory(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phone) VALUES (?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()
            self.tbox.insert(END, "\nInserted " + str(self.name) + " into the database with code " + str(self.id_e.get()))
            tkinter.messagebox.showinfo('sucess','succed')

root = Tk()
b = Database(root)
root.geometry('1920x1080+0+0')
root.title('add to the database')
root.mainloop()

