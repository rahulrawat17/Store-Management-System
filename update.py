from tkinter import *
import tkinter.messagebox
import sqlite3
conn = sqlite3.connect('store.db')
c = conn.cursor()

class Update:
    def __init__(self,master,*args,**kwargs):
        
        self.master = master
        self.heading = Label(master, text ='>> UPDATE <<', font =('arial 40 bold'), fg ='blue')
        self.heading.place(x=400,y=0)
        
        #labels for entries for the window
        self.id_l_f = Label(master, text ='Enter ID', font =('arial 18 bold'))
        self.id_l_f.place(x=20,y=100)
        self.or_l_f = Label(master, text ='OR', font =('arial 18 bold'))
        self.or_l_f.place(x=450,y=140)
        self.name_1_f = Label(master, text ='Enter Product Name', font =('arial 18 bold'))
        self.name_1_f.place(x=20,y=180)
        self.name_1 = Label(master, text ='Product Name*', font =('arial 18 bold'))
        self.name_1.place(x=20,y=270)
        self.stock_l = Label(master, text ='Stocks*', font =('arial 18 bold'))
        self.stock_l.place(x=20,y=320)
        self.cp_l = Label(master, text ='Cost Price*', font =('arial 18 bold'))
        self.cp_l.place(x=20,y=370)
        self.sp_l = Label(master, text ='Selling Price*', font =('arial 18 bold'))
        self.sp_l.place(x=20,y=420)
        self.vendor_l = Label(master, text ='Total CP', font =('arial 18 bold'))
        self.vendor_l.place(x=20,y=470)
        self.vendor_l = Label(master, text ='Total SP', font =('arial 18 bold'))
        self.vendor_l.place(x=20,y=520)
        self.vendor_l = Label(master, text ='Assumed Profit', font =('arial 18 bold'))
        self.vendor_l.place(x=20,y=570)
        self.vendor_l = Label(master, text ='Vendor Name', font =('arial 18 bold'))
        self.vendor_l.place(x=20,y=620)
        self.vendor_phone_l = Label(master, text ='Vendor Phone no.', font =('arial 18 bold'))
        self.vendor_phone_l.place(x=20,y=670)
        self.t_c = Label(master, text ='*input required', font =('arial 15'))
        self.t_c.place(x=20,y=720)
        
        self.logo = Label(master, text ='>> RS STORE <<', font =('arial 40 bold'), fg ='red')
        self.logo.place(x=970,y=580)
        
        #entries for searching labels
        self.id_s_e = Entry(master, width= 25, font =('arial 18 bold'))
        self.id_s_e.place(x=320,y=100)
        self.id_s_e.focus()
        self.name_s_e = Entry(master, width =25, font =('arial 18 bold'))
        self.name_s_e.place(x=320,y=180)

        #update entries label
        self.name_e = Entry(master, width =25, font =('arial 18 bold'))
        self.name_e.place(x=320,y=270)
        self.stock_e = Entry(master, width =25, font =('arial 18 bold'))
        self.stock_e.place(x=320,y=320)
        self.stock_e.focus()
        self.cp_e = Entry(master, width =25, font =('arial 18 bold'))
        self.cp_e.place(x=320,y=370)
        self.sp_e = Entry(master, width =25, font =('arial 18 bold'))
        self.sp_e.place(x=320,y=420)
        self.total_cp_e = Entry(master, width =25, font =('arial 18 bold'))
        self.total_cp_e.place(x=320,y=470)
        self.total_sp_e = Entry(master, width =25, font =('arial 18 bold'))
        self.total_sp_e.place(x=320,y=520)
        self.assumed_profit_e = Entry(master, width =25, font =('arial 18 bold'))
        self.assumed_profit_e.place(x=320,y=570)
        self.vendor_e = Entry(master, width =25, font =('arial 18 bold'))
        self.vendor_e.place(x=320,y=620)
        self.vendor_phone_e = Entry(master, width =25, font =('arial 18 bold'))
        self.vendor_phone_e.place(x=320,y=670)
        
        #button to search
        self.btn_add = Button(master, text ='Search', width =20, height =2, bg ='steelblue', fg ='white', command = self.search)
        self.btn_add.place(x=720,y=130)
        
        #button to update
        self.btn_add = Button(master, text ='Update', width =20, height =2, bg ='steelblue', fg ='white', command = self.update)
        self.btn_add.place(x=720,y=660)
    
        
    def search(self, *args, **kwargs):
        if self.id_s_e.get() != '' :
            sql = "SELECT * FROM INVENTORY WHERE id=?"
            result = c.execute(sql, (self.id_s_e.get(), ))
            for r in result:
                self.n1 = r[1] #name
                self.n2 = r[2] #stock
                self.n3 = r[3] #cp
                self.n4 = r[4] #sp
                self.n5 = r[5] #totsl_cp
                self.n6 = r[6] #total_sp
                self.n7 = r[7] #assumed_profit
                self.n8 = r[8] #vendor_name
                self.n9 = r[9] #vendor_phone
            conn.commit()
            
        elif self.name_s_e.get() != '' :
            sql = "SELECT * FROM INVENTORY WHERE name=?"
            result = c.execute(sql, (self.name_s_e.get(), ))
            for r in result:
                self.n1 = r[1] #name
                self.n2 = r[2] #stock
                self.n3 = r[3] #cp
                self.n4 = r[4] #sp
                self.n5 = r[5] #total_cp
                self.n6 = r[6] #total_sp
                self.n7 = r[7] #assumed_profit
                self.n8 = r[8] #vendor_name
                self.n9 = r[9] #vendor_phone
                
            conn.commit()
        else:
            tkinter.messagebox.showinfo('warning','enter input')
                
        #clear fileds
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        
        self.total_cp_e.delete(0, END)
        self.total_sp_e.delete(0, END)
        self.assumed_profit_e.delete(0, END)

        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        
        #insert into entries to update        
        self.name_e.insert(0, str(self.n1))
        self.stock_e.insert(0, str(self.n2))
        self.cp_e.insert(0, str(self.n3))
        self.sp_e.insert(0, str(self.n4))

        self.total_cp_e.insert(0, str(self.n5))
        self.total_sp_e.insert(0, str(self.n6))
        self.assumed_profit_e.insert(0, str(self.n7))

        self.vendor_e.insert(0, str(self.n8))
        self.vendor_phone_e.insert(0, str(self.n9))

    def update(self, *args, **kwargs):
        #get all the updated values
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.total_cp_e.get()
        self.u6 = self.total_sp_e.get()
        self.u7 = self.assumed_profit_e.get()
        self.u8 = self.vendor_e.get()
        self.u9 = self.vendor_phone_e.get()


        #dynamic entries
        self.u5 = float(self.u3) * float(self.u2)
        self.u6 = float(self.u4) * float(self.u2)
        self.u7 = float(self.u6 - self.u5)


        query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, assumed_profit=?, vendor=?, vendor_phone=? WHERE name=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4,self.u5, self.u6, self.u7, self.u8, self.u9, self.name_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo('Success','Updated')
        
root = Tk()

b = Update(root)
root.geometry('1920x1080+0+0')
root.title('Update')
root.mainloop()
