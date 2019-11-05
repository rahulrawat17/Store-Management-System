from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import time
import math
import os
import random

time_full = time.ctime()
time_list = time_full.split()
time_hms = time_list[3]
time_hmss = time_hms.split(':')
time_h = time_hmss[0]
time_m = time_hmss[1]
time_s = time_hmss[2]
final_time = time_h + '_' + time_m + '_' + time_s

conn = sqlite3.connect('store.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT, quantity INTEGER, amount INTEGER, date TEXT)')


#date
date = datetime.datetime.now().date()

#temporary lists like sessions
product_list = []
product_price =[]
product_quantity = []
product_id =[]

#list for labels
labels_list = []

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        
        #frames
        self.left = Frame(master, width ='900', height ='1080', bg ='white')
        self.left.pack(side=LEFT)
        
        self.right = Frame(master, width ='800', height = '1080', bg ='lightblue')
        self.right.pack(side=RIGHT)
        
        #components
        self.heading = Label(self.left, text ='>> RS Store <<', font =('arial 40 bold'), fg ='red', bg ='white')
        self.heading.place(x=270,y=0)
        
        self.date_l = Label(self.right, text ="Today's date - " + str(date), font =('arial 16 bold'), bg ='lightblue', fg ='black')
        self.date_l.place(x=10,y=0)
        
        
        #table invoice..
        self.tproduct = Label(self.right, text ='Products', font =('arial 17 bold'), bg ='lightblue', fg ='white')
        self.tproduct.place(x=0,y=50)
        self.tquantity = Label(self.right, text ='Quantity', font =('arial 17 bold'), bg ='lightblue', fg ='white')
        self.tquantity.place(x=300,y=50)
        self.tamount = Label(self.right, text ='Amount', font =('arial 17 bold'), bg ='lightblue', fg ='white')
        self.tamount.place(x=500,y=50)
        
        #enter stuff
        self.enterid = Label(self.left, text ='Enter Product id', font =('arial 18 bold'), bg ='white')
        self.enterid.place(x=0,y=90)
        
        self.enteride = Entry(self.left, width =25, font =('arial 18 bold'), bg ='lightblue')
        self.enteride.place(x=220,y=90)
        self.enteride.focus()
        
        #buton
        self.search_btn = Button(self.left, text ='Search', width =22, height =2, bg ='orange', command =self.ajax)
        self.search_btn.place(x=350,y=140)
        
        #fill it later by ajex function
        self.productname = Label(self.left, text ='', font =('arial 25 bold'), bg ='white', fg ='blue')
        self.productname.place(x=0,y=250)
        self.pprice = Label(self.left, text ='', font =('arial 25 bold'), bg ='white', fg ='blue')
        self.pprice.place(x=0,y=325)
        
        #total label
        self.total_l = Label(self.right, text ='', font =('arial 40 bold'), bg ='lightblue', fg ='white')
        self.total_l.place(x=0,y=620)

        #key binding...
        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.add_cart)
        self.master.bind("<Down>", self.generate_bill)
        #test#self.master.bind("<Down>", self.change1)

    #test#def change1():
        #test#self.change_e.focus()
        
    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        #get the product info
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for r in result:
            self.get_id = r[0]
            self.get_name = r[1]
            self.get_price = r[4]
            self.get_stock = r[2]
            
        self.productname.configure(text = "Product's Name : " + str(self.get_name))
        self.pprice.configure(text = "Price : Rs. " + str(self.get_price))
        
        #create the quantity
        self.quantity_l = Label(self.left, text ='Enter quantity', font =('arial 18 bold'), bg ='white')
        self.quantity_l.place(x=0,y=400)
        
        self.quantity_e = Entry(self.left, width =10, font =('arial 18 bold'), bg ='lightblue')
        self.quantity_e.place(x=200,y=400)
        self.quantity_e.focus()
        
        #add to cart
        self.add_cart_btn = Button(self.left, text ='Add to Cart', width =22, height =2, bg ='orange',command =self.add_cart)
        self.add_cart_btn.place(x=350,y=450)
        
        #generate bill and change
        self.change_l = Label(self.left, text ='Given Amount', font =('arial 18 bold'), bg ='white')
        self.change_l.place(x=0,y=530)
        self.change_e = Entry(self.left, font =('arial 18 bold'), bg ='light blue')
        self.change_e.place(x=200,y=530)
        
        #button for change
        self.change_btn = Button(self.left, text ='Change', width =22, height =2, bg ='orange', command =self.change_func)
        self.change_btn.place(x=350,y=570)
        
        #generate bill button
        self.bill_btn = Button(self.left, text ='Generate Bill', width =90, height =3, bg='red', command =self.generate_bill)
        self.bill_btn.place(x=0,y=670)
    
    def add_cart(self, *args, **kwargs):
        #get the quantity value and from the database
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo('error','not that much product available')
        else:
            #calculate the price
            self.final_price = float(self.quantity_value) * float(self.get_price)
            product_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)
            
            self.x_i =0
            self.y_i =100
            self.c =0
            
            for self.p in product_list:
                self.tempname = Label(self.right, text =str(product_list[self.c]), font =('arial 18 bold'), bg ='lightblue', fg ='grey')
                self.tempname.place(x=0, y=self.y_i)
                labels_list.append(self.tempname)
                
                self.tempqt = Label(self.right, text =str(product_quantity[self.c]), font =('arial 18 bold'), bg ='lightblue', fg ='grey')
                self.tempqt.place(x=300,y=self.y_i)
                labels_list.append(self.tempqt)
                
                self.tempprice = Label(self.right, text =str(product_price[self.c]), font =('arial 18 bold'), bg ='lightblue', fg ='grey')
                self.tempprice.place(x=500,y=self.y_i)
                labels_list.append(self.tempprice)
                
                
                self.temptotal = Label(self.right, text =product_price[self.c] , font =('arial 18 bold'), bg ='lightblue', fg ='white')
                self.y_i += 40
                self.c += 1

                #total configure
                self.total_l.configure(text='Total: Rs.' + str(sum(product_price)))

                #delete
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.productname.configure(text ='')
                self.pprice.configure(text ='')
                self.add_cart_btn.destroy()

                #focus
                self.enteride.focus()
                self.enteride.delete(0, END)
                
    def change_func(self, *args, **kwargs):
        #get
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))
        
        self.to_give = self.amount_given - self.our_total
        
        #label
        self.c_amount = Label(self.left, text ='Change : Rs. ' + str(self.to_give), font = ('arial 18 bold'), bg ='white', fg ='red')
        self.c_amount.place(x=0,y=600)
            
    def generate_bill(self, *args, **kwargs):
        #create the bill before updating to the database
        directory = "D:/store/invoice/" + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        #templates for the bill
        company = "\t\t   R.S Company Pvt. Ltd.\n"
        address = "\t\t   Nirman Vihar, Delhi\n"
        phone = "\t\t\t8076337520\n"
        sample = "\t\t\t--Invoice--\n"
        dt = "\t\t\t" + str(date)
        
        table_header = "\n\n\t---------------------------------------\n\tSN.\tProducts\tQty\tAmount\n\t---------------------------------------"
        final = company + address + phone + sample + dt + '\n' + table_header
        
        #open a file to write it to
        file_name = str(directory) + final_time + '.txt'
        f = open(file_name, 'w')
        f.write(final)
        
        #fill dynamics
        r = 1
        i = 0
        for t in product_list:
            f.write("\n\t" + str(r) + '\t' + str(product_list[i] + '        ')[:9] + "\t" + str(product_quantity[i]) + "\t" + str(product_price[i]))
            i += 1
            r += 1
        f.write("\n\n\tTotal: Rs. " + str(sum(product_price)))
        f.write("\n\tThanks visit again :)")
        f.close()

        #print the bill....................................................................................................................
        #os.startfile(file_name, "print")

                
        #decrease the stock
        self.x = 0
        
        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x], ))
        
        for i in product_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(product_quantity[self.x])
            
            #updating the stocks
            sql ="UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()
            
            #insert in transaction table
            sql2 = "INSERT INTO transactions(product_name, quantity, amount, date) VALUES (?,?,?,?)"
            c.execute(sql2, (product_list[self.x], product_quantity[self.x], product_price[self.x], date))
            conn.commit()
            
            self.x += 1
            
        for a in labels_list:
            a.destroy()
            
        del(product_list[:])
        del(product_id[:])
        del(product_quantity[:])
        del(product_price[:])
        self.total_l.configure(text='')
        self.c_amount.configure(text='')
        self.change_e.delete(0, END)
        
        self.enteride.focus()
        
        tkinter.messagebox.showinfo('success','Bill Printed Successfully')
        
root =Tk()
b = Application(root)

root.geometry('1920x1080+0+0')
root.mainloop()
