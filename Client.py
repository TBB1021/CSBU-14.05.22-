import sqlite3
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import smtplib, ssl
import ctypes
import re
class Main():
    def __init__(self,master):
        self.master = master
        self.master.geometry('1000x400')
        self.master.title('Clients')
        self.Table()
        self.stack=Stack()
        self.add=Button(self.master,text="Add",command=self.Add,width=12,fg="green").place(x=700,y=350)
        self.remove=Button(self.master,text="Remove",command=self.Remove,width=12,fg="green").place(x=250,y=350)
        self.back=Button(self.master,text="Back",command=self.Back,width=12,fg="green").place(x=400,y=350)
        self.info=Button(self.master,text="Infomation",command=self.Info,width=12,fg="green").place(x=550,y=350)
        undoact=Button(self.master,text="Undo",command=self.Rpop,width=12,fg="green").place(x=350,y=250)
        peak=Button(self.master,text="Peak",command=lambda x=self.stack:Stack.Peak(x),width=12,fg="green").place(x=500,y=250)
        size=Button(self.master,text="Size",command=lambda x=self.stack:Stack.Size(x),width=12,fg="green").place(x=650,y=250)
    
    def Add(self):
        root3=Toplevel(self.master)
        AddGui=AddPage(root3,self.Trainer_ID,self.tree,self.stack)
    
    def Table(self):
        self.Rlog()
        self.tree= ttk.Treeview(column=(self.master,"column1", "column2", "column3", "column4"), show='headings')
        self.tree.heading("#1", text="ClientID")
        self.tree.heading("#2", text="Trainer_ID")
        self.tree.heading("#3", text="Forename")
        self.tree.heading("#4", text="Surname")
        self.tree.heading("#5", text="Password")
        self.tree.grid(row=7,column=3)
        try:
            with  sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT ClientID,Trainer_ID,Forename,Surname,Password FROM Clients WHERE Trainer_ID=?"
                cursor.execute(sql,(self.Trainer_ID,))
                rows=cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)
        except:
            pass
        self.tree.bind("<Double-1>", self.Copy)
        self.tree.bind("<1>", self.Copy)
    
    def Rpop(self):
        Stack.Pop(self.stack)
        Main.Restart(self)
    
    def Back(self):
        self.master.destroy()
    
    def Info(self):
        root2=Toplevel()
        InfoGui=InfoPage(root2,self.values,self.tree,self.Trainer_ID,self.stack)
    
    def Copy(self,event):
        record = self.tree.focus()
        self.values=self.tree.item(record,'values')
        print(self.values)
    
    def Remove(self):
        ClientID=self.values[0]
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            data="SELECT * FROM Clients INNER JOIN Info ON Clients.ClientID=info.ClientID AND Clients.ClientID=?"
            sql='DELETE FROM Clients WHERE ClientID=?'
            sql2='DELETE FROM Info WHERE ClientID=?'
            cursor.execute(data,(ClientID,))
            self.data=cursor.fetchall()
            cursor.execute(sql,(ClientID,))
            cursor.execute(sql2,(ClientID,))
        x=["DELETE",self.data]
        Stack.Append(self.stack,x)
        Main.Restart(self)
            
    
    def Rlog(self):
        with  sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT Trainer_ID FROM Log ORDER BY Record DESC LIMIT 1"
            cursor.execute(sql)
            Trainer=cursor.fetchall()
            self.Trainer_ID=str(Trainer[0][0])
    
    def Restart(self):
        self.tree.delete(*self.tree.get_children())
        with  sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT ClientID,Trainer_ID,Forename,Surname,Password FROM Clients WHERE Trainer_ID=?"
                cursor.execute(sql,(self.Trainer_ID,))
                rows=cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)

class InfoPage():
    def __init__(self,master,values,tree,Trainer_ID,stack):
        self.master = master
        self.tree=tree
        self.Trainer_ID=Trainer_ID
        self.stack=stack
        self.master.geometry('500x250')
        self.master.title('Information')
        self.fore=StringVar()
        self.sur=StringVar()
        self.password=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.dob=StringVar()
        self.address=StringVar()
        self.Sheight=StringVar()
        self.Sweight=StringVar()
        self.Scalorie=StringVar()
        self.sex=StringVar()
        weight=[]
        for x in range(70,101):
            weight.append(x)
        
        forl=Label(self.master,text="Forename:",).place(x=50,y=25)
        forbx=Entry(self.master,textvariable=self.fore,width=15).place(x=50,y=45)
        surl=Label(self.master,text="Surname:").place(x=150,y=25)
        surbx=Entry(self.master,textvariable=self.sur,width=15).place(x=150,y=45)
        pasl=Label(self.master,text="Password:").place(x=250,y=25)
        pasbx=Entry(self.master,textvariable=self.password,width=15).place(x=250,y=45)
        phol=Label(self.master,text="Phone:").place(x=350,y=25)
        phobx=Entry(self.master,textvariable=self.phone,width=15).place(x=350,y=45)
        emal=Label(self.master,text="Email:").place(x=100,y=70)
        emabx=Entry(self.master,textvariable=self.email,width=15).place(x=100,y=90)
        DOBl=Label(self.master,text="DOB:",).place(x=200,y=70)
        DOBbx=DateEntry(self.master,textvariable=self.dob, width=12, background='Black',foreground='Orange').place(x=200,y=90)
        adsl=Label(self.master,text="Address:").place(x=300,y=70)
        adsbx=Entry(self.master,textvariable=self.address,width=15).place(x=300,y=90)
        heil=Label(self.master,text="Height(Feet):").place(x=50,y=115)
        heibx=Entry(self.master,textvariable=self.Sheight,width=15).place(x=50,y=135)
        weil=Label(self.master,text="Weight(Kg):").place(x=150,y=115)
        weibx = OptionMenu(self.master,self.Sweight,*weight).place(x=150,y=135)
        call=Label(self.master,text="Aver. Calorie:").place(x=250,y=115)
        calbx=Entry(self.master,textvariable=self.Scalorie,width=15).place(x=250,y=135)
        sexl=Label(self.master,text="Sex:").place(x=350,y=115)
        sexbx=Entry(self.master,textvariable=self.sex,width=15).place(x=350,y=135)
        try:
            self.ClientID=values[0]
            self.edit=Button(self.master,text="Edit",command=self.Edit,width=12,fg="Black").place(x=200,y=170)
            tcl=Label(self.master,text="ClientID:"+self.ClientID).place(x=220,y=200)
            self.GetInfo()
        except:
            pass
    
    def GetInfo(self):
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT * FROM Clients INNER JOIN Info ON Clients.ClientID=info.ClientID AND Clients.ClientID=?"
            cursor.execute(sql,(self.ClientID,))
            self.data=list(cursor.fetchall()[0])
            print(self.data)
        self.info_ID=self.data[9]
        self.fore.set(self.data[2])
        self.sur.set(self.data[3])
        self.password.set(self.data[4])
        self.phone.set(self.data[5])
        self.email.set(self.data[6])
        self.dob.set(self.data[7])
        self.address.set(self.data[8])
        self.Sheight.set(self.data[11])
        self.Sweight.set(self.data[12])
        self.Scalorie.set(self.data[13])
        self.sex.set(self.data[14])
    
    def Edit(self):
        error=False
        Forename=self.fore.get()
        Surname=self.sur.get()
        Password=self.password.get()
        Phone=self.phone.get()
        Email=self.email.get()
        DOB=self.dob.get()
        Address=self.address.get()
        Height=self.Sheight.get()
        Weight=self.Sweight.get()
        Calorie=self.Scalorie.get()
        Sex=self.sex.get()
        if re.search(r'^[A-Z][a-z]+$',Forename):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.fore.set("Invalid")
        if re.search(r'^([A-Z][a-z]+)|([A-Z][a-z]+-[A-Z][a-z]+)$',Surname):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.sur.set("Invalid")
        if re.search(r'[A-Z]+[a-z]+[0-9]?',Password):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.password.set("Invalid")
        if re.search(r'^(07|\+447)[0-9]{9}$',Phone):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.phone.set("Invalid")
        if re.search(r'[A-Za-z0-9]+@(gmail|outlook|yahoo{1})\.(com|edu|gov){1}',Email):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.email.set("Invalid")
        if re.search(r'[0-9]{1,5}\s[A-Z][a-z]+\s(street|lane|road|avenue)',Address):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.address.set("Invalid")
        if re.search(r'([0-9]\'[0-9]{1,2})|([0-9] [0-9]{1,2})',Height):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.Sheight.set("Invalid")
        if re.search(r'([0-9]{4})',Calorie):
            if error==True:
                error=True
            elif error==False:
                error=False
        else:
            error=True
            self.Scalorie.set("Invalid")
        if error==False:
            with sqlite3.connect("DATABASEV1.db") as db:
                cursor=db.cursor()
                sql="UPDATE Clients SET Forename=?,Surname=?,Password=?,Phone=?,Email=?,DOB=?,Address=? WHERE ClientID=?"
                cursor.execute(sql,(Forename,Surname,Password,Phone,Email,DOB,Address,self.ClientID,))
            with sqlite3.connect("DATABASEV1.db") as db:
                cursor=db.cursor()
                sq2="UPDATE Info SET Height=?,Weight=?,Calorie =?,Sex=? WHERE info_ID=?"
                cursor.execute(sq2,(Height,Weight,Calorie,Sex,self.info_ID,))
            x=["UPDATE",self.data]
            Stack.Append(self.stack,x)
            Main.Restart(self)
            self.master.destroy()

class AddPage(InfoPage):   
    def __init__(self,InfoPage,Trainer_ID,tree,stack):
        self.values=[]
        self.Trainer_ID=Trainer_ID
        self.tree=tree
        self.stack=stack
        super().__init__(InfoPage,self.values,self.tree,self.Trainer_ID,self.stack)
        self.add=Button(self.master,text="Add Client",command=self.Add,width=12,fg="green").place(x=188,y=170)
        self.Sheight.set("")
        self.Sweight.set("")
        self.Scalorie.set("")
        self.sex.set("")
        self.fore.set("")
        self.sur.set("")
        self.password.set("")
        self.phone.set("")
        self.email.set("")
        self.dob.set("")
        self.address.set("")
    
    def Add(self):
        self.ClientID=random.randint(1000,1999)
        self.InfoID=random.randint(500,599)
        Forename=self.fore.get()
        Surname=self.sur.get()
        Password=self.password.get()
        Phone=self.phone.get()
        Email=self.email.get()
        DOB=self.dob.get()
        Address=self.address.get()
        Height=self.Sheight.get()
        Weight=self.Sweight.get()
        Calorie=self.Scalorie.get()
        Sex=self.sex.get()
        self.data=[self.ClientID,self.Trainer_ID]
        error=False
        if re.search(r'^[A-Z][a-z]+$',Forename):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Forename)
        else:
            error=True
            self.fore.set("Invalid")
        if re.search(r'^([A-Z][a-z]+)|([A-Z][a-z]+-[A-Z][a-z]+)$',Surname):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Surname)
        else:
            error=True
            self.sur.set("Invalid")
        if re.search(r'[A-Z]+[a-z]+[0-9]?',Password):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Password)
        else:
            error=True
            self.password.set("Invalid")
        if re.search(r'^(07|\+447)[0-9]{9}$',Phone):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Phone)
        else:
            error=True
            self.phone.set("Invalid")
        if re.search(r'[A-Za-z0-9]+@(gmail|outlook|yahoo{1})\.(com|edu|gov){1}',Email):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Email)
        else:
            error=True
            self.email.set("Invalid")
        if re.search(r'[0-9]{1,5}\s[A-Z][a-z]+\s(street|lane|road|avenue)',Address):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Address)
                self.data.append(self.InfoID)
        else:
            error=True
            self.address.set("Invalid")
        if re.search(r'([0-9]\'[0-9]{1,2})|([0-9] [0-9]{1,2})',Height):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Height)
        else:
            error=True
            self.Sheight.set("Invalid")
        if re.search(r'([0-9]{4})',Calorie):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Calorie)
        else:
            error=True
            self.Scalorie.set("Invalid")
        if re.search(r'(trans)?[M|F]{1}',Sex):
            if error==True:
                error=True
            elif error==False:
                error=False
                self.data.append(Sex)
        else:
            error=True
            self.sex.set("Invalid")
        if error==False:
            with sqlite3.connect("DATABASEV1.db") as db:
                cursor=db.cursor()
                sql="INSERT INTO Clients(ClientID,Trainer_ID,Forename,Surname,Password,Phone,Email,DOB,Address) VALUES(?,?,?,?,?,?,?,?,?)"
                cursor.execute(sql,(self.ClientID,self.Trainer_ID,Forename,Surname,Password,Phone,Email,DOB,Address,))
            with sqlite3.connect("DATABASEV1.db") as db:
                cursor=db.cursor()
                sql="INSERT INTO Info(info_ID,ClientID,Height,Weight,Calorie,Sex) VALUES(?,?,?,?,?,?)"
                cursor.execute(sql,(self.InfoID,self.ClientID,Height,Weight,Calorie,Sex))
            __Gympass="Shiftgym10101"
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com",context=context) as server:
                server.login("shiftgymleisure@gmail.com", __Gympass)
                __sender_email = "shiftgymleisure@gmail.com"
                __receiver_email =Email
                __message = """\
                            Subject: Welcome 

                            
                                    Welcome to SHIFT Gym and Leisure centre
                                    You unique identification number is """+ str(self.ClientID)+"""."""
                server.sendmail(__sender_email, __receiver_email, __message)
            x=["ADD",self.data]
            Stack.Append(self.stack,x)
            Main.Restart(self)
            self.master.destroy()

class Stack():
    def __init__(self):
        self.stack=[]
        self.size=0
        self.pointer=-1
    
    def Append(self,x):
        self.stack.append(x)
        self.size=self.size+1
        self.pointer=self.pointer+1
        
    
    def Pop(self):
        if self.size==0:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, "Stack Is Empty (Underflow error)", 'Client Stack', ) 
        elif self.size>0:
            undo=self.stack[self.pointer]
            self.stack.pop(self.pointer)
            self.pointer=self.pointer-1
            self.size=self.size-1
            if undo[0]=="UPDATE":
                print("here")
                with sqlite3.connect("DATABASEV1.db") as db:
                    cursor=db.cursor()
                    sql="UPDATE Clients SET Forename=?,Surname=?,Password=?,Phone=?,Email=?,DOB=?,Address=? WHERE ClientID=?"
                    cursor.execute(sql,(undo[1][2],undo[1][3],undo[1][4],undo[1][5],undo[1][6],undo[1][7],undo[1][8],undo[1][0]))
                    sq2="UPDATE Info SET Height=?,Weight=?,Calorie=?,Sex=? WHERE info_ID=?"
                    cursor.execute(sq2,(undo[1][11],undo[1][12],undo[1][13],undo[1][14],undo[1][9],))
            elif undo[0]=="ADD":
                sql1="DELETE FROM Clients WHERE ClientID=?"
                sql2="DELETE FROM Info WHERE ClientID=?"
                with sqlite3.connect("DATABASEV1.db") as db:
                    cursor=db.cursor()
                    cursor.execute(sql1,(undo[1][0],))
                    cursor.execute(sql2,(undo[1][10],))
            elif undo[0]=="DELETE":
                sql1="INSERT INTO Clients(ClientID,Trainer_ID,Forename,Surname,Password,Phone,Email,DOB,Address) VALUES(?,?,?,?,?,?,?,?,?)"
                sql2="INSERT INTO Info(Info_ID,ClientID,Height,Weight,Calorie,Sex) VALUES(?,?,?,?,?,?)"
                print(undo[1][0][0])
                with sqlite3.connect("DATABASEV1.db") as db:
                    cursor=db.cursor()
                    cursor.execute(sql1,(undo[1][0][0],undo[1][0][1],undo[1][0][2],undo[1][0][3],undo[1][0][4],undo[1][0][5],undo[1][0][6],undo[1][0][7],undo[1][0][8]))                    
                    cursor.execute(sql2,(undo[1][0][9],undo[1][0][10],undo[1][0][11],undo[1][0][12],undo[1][0][13],undo[1][0][14]))
    def Peak(self):
        if self.pointer>-1:
            action=self.stack[self.pointer]
            actions=str(action[0])+" "+str(action[1][2])+" "+str(action[1][3])
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, "The next action to be undone is "+actions, 'Client Stack', ) 
        elif self.pointer==-1:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, "Stack Is Empty (Underflow error)", 'Client Stack', ) 
    def Size(self):
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, "The stack has "+str(self.size)+" actions that can be done", 'Client Stack', ) 
        
def main():
    root=Tk()
    myGUI=Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
