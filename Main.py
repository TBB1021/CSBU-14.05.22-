from tkinter import *
from tkcalendar import *
from subprocess import call
from  tkinter import ttk
from threading import *
import smtplib, ssl
import tkinter
import datetime
import sqlite3
import random
import string
import ctypes
import os
import re

class Mainwindow():
    def __init__(self,master):
        self.master = master
        self.master.geometry('500x200')
        self.master.title("Welcome Page")
        self.welcometxt=Label(self.master,text="Welcome to the SHIFT gym management system",width=0,fg="black").place(x=125,y=60)
        self.login=Button(self.master,text="Login",command=self.Login,width=15).place(x=270,y=130)
        self.sign=Button(self.master,text="Sign Up",command=self.SignUp,width=15).place(x=125,y=130)
        self.quit=Button(self.master,text="Close",command=self.Quit,width=15).place(x=200,y=165)
    def Login(self):
        root2=Toplevel(self.master)
        myGui=LoginPage(root2)
    def SignUp(self):
        root3=Toplevel(self.master)
        myGui=SignUpPage(root3)
    def Quit(self):
        self.master.destroy()

class LoginPage():
    def  __init__(self,master):
        self.master=master
        self.master.title("Login Page")
        self.master.geometry('250x150')
        self.id=StringVar()
        self.password=StringVar()
        self.Id=Label(self.master,text="Trainer ID:",width=12,fg="green").place(x=20,y=50)
        self.detail=Label(self.master,text="Please enter your security details",width=30,fg="black").place(x=20,y=10)
        self.IdBox=Entry(self.master,textvariable=self.id,width=18).place(x=100,y=50)
        self.Pass=Label(self.master,text="Password:",width=12,fg="green").place(x=20,y=70)
        self.PassBox=Entry(self.master,textvariable=self.password,width=18).place(x=100,y=72)
        self.back=Button(self.master,text="Back",command=self.Back,width=12).place(x=30,y=100)
        self.enter=Button(self.master,text="Log in",command=self.Login,width=12).place(x=130,y=100)
    def Back(self):
        self.master.destroy()
    def Login(self):
        self.Trainer_ID=self.id.get()
        Password=self.password.get()
        with  sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT Password FROM Trainers WHERE Trainer_ID=?"
            cursor.execute(sql,(self.Trainer_ID,))
            x=cursor.fetchall()
            if len(x)==0:
                MessageBox = ctypes.windll.user32.MessageBoxW
                MessageBox(None, "Please enter correct security details", 'Log In', )   
            elif ((x[0][0]))==(Password):
                x=datetime.datetime.now()
                Date=x.strftime("%x")
                Time=x.strftime("%X")
                Reason="Log In"
                sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
                cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
                self.home()
        

    def home(self):
        root4=Toplevel(self.master)
        myGui=HomePage(root4,self.Trainer_ID)       

class SignUpPage():
    def __init__(self,master):
        self.master=master
        self.master.title("Sign Up Page")
        self.master.geometry('400x200')
        self.sur=StringVar()
        self.fore=StringVar()
        self.password=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.dob=StringVar()
        self.address=StringVar()
        self.sex=StringVar()
        forel=Label(self.master,text="Forename:").place(x=60,y=15)
        surl=Label(self.master,text="Surname:").place(x=60,y=35)
        pasl=Label(self.master,text="Password:").place(x=60,y=55)
        phol=Label(self.master,text="Phone:").place(x=60,y=75)
        self.forebx=Entry(self.master,textvariable=self.fore,width=10)
        self.forebx.place(x=125,y=15)
        self.surbx=Entry(self.master,textvariable=self.sur,width=10)
        self.surbx.place(x=125,y=35)
        self.passwordbx=Entry(self.master,textvariable=self.password,width=10)
        self.passwordbx.place(x=125,y=55)
        self.phonebx=Entry(self.master,textvariable=self.phone,width=10)
        self.phonebx.place(x=125,y=75)
        dobl=Label(self.master,text="DOB:").place(x=210,y=15)
        eml=Label(self.master,text="Email:").place(x=210,y=35)
        adrl=Label(self.master,text="Address:").place(x=210,y=55)
        sexl=Label(self.master,text="Sex:").place(x=210,y=75)
        dobbx = DateEntry(self.master,textvariable=self.dob, width=10, background='Black',foreground='Orange', borderwidth=2).place(x=275,y=15)
        self.emailbx=Entry(self.master,textvariable=self.email,width=10)
        self.emailbx.place(x=275,y=35)
        self.addressbx=Entry(self.master,textvariable=self.address,width=10)
        self.addressbx.place(x=275,y=55)
        self.sexbx=Entry(self.master,textvariable=self.sex,width=10)
        self.sexbx.place(x=275,y=75)
        signup=Button(self.master,text="Sign Up",command=self.Sign,width=12).place(x=175,y=115)
    def Sign(self):
        error=7
        ARI=False
        self.Trainer_ID=random.randint(3000,3999)
        Forename=self.fore.get()
        Surname=self.sur.get()
        Password=self.password.get()
        Phone=self.phone.get()
        BEmail=self.email.get()
        DOB=self.dob.get()
        Address=self.address.get()
        Sex=self.sex.get()
        if re.search(r'^[A-Z][a-z]+$',Forename):
            self.forebx.config(bg='white')
            self.forebx.config(fg='green')
            if error>0:
                error=error-1
        else:
            self.forebx.config(bg='red')
            self.forebx.config(fg='white')
        if re.search(r'^[A-Z][a-z]+$',Surname):
            self.surbx.config(bg='white')
            self.surbx.config(fg='green')
            if error>0:
                error=error-1
        else:
            self.surbx.config(bg='red')
            self.surbx.config(fg='white')
        if re.search(r'[A-Z]+[a-z]+[0-9]?',Password):
            self.passwordbx.config(bg='white')
            self.passwordbx.config(fg='green')
            if error>0:
                error=error-1
        else:
            self.passwordbx.config(bg='red')
            self.passwordbx.config(fg='white')
        if re.search(r'^(07|\+447)[0-9]{9}$',Phone):
            self.phonebx.config(bg='white')
            self.phonebx.config(fg='green')
            if error>0:
                error=error-1
        else:
            self.phonebx.config(bg='red')
            self.phonebx.config(fg='white')
        if re.search(r'([A-Za-z0-9]+@[a-z]+\.[a-z]{3})',BEmail):
            self.emailbx.config(bg='white')
            self.emailbx.config(fg='green')
            if error>0:
                error=error-1
        else:
            self.emailbx.config(bg='red')
            self.emailbx.config(fg='white')
        if re.search(r'[0-9]{1,5}\s[A-Z][a-z]+\s[a-z]+',Address):
            self.addressbx.config(bg='white')
            self.addressbx.config(fg='green')
            if error>0:
                error=error-1
        else:
            self.addressbx.config(bg='red')
            self.addressbx.config(fg='white') 
        if re.search(r'((M|F)|(m|f)){1}',Sex):
            self.sexbx.config(bg='white')
            self.sexbx.config(fg='green')
            if error>0:
                error=error-1
        else:
            self.sexbx.config(bg='red')
            self.sexbx.config(fg='white') 
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT Trainer_ID,Phone,BEmail FROM Trainers"
            cursor.execute(sql)
            compare=cursor.fetchall()
        for x in range (len(compare)):
            if self.Trainer_ID==compare[x][0] and Phone==compare[x][1] or BEmail==compare[x][2]:
                ARI=True
            elif self.Trainer_ID==compare[x][0] and Phone!=compare[x][1] and BEmail!=compare[x][2]:
                self.Trainer_ID=random.randint(3000,3999)
                ARI=False
            elif self.Trainer_ID!=compare[x][0] and Phone!=compare[x][1] and BEmail!=compare[x][2]:
                ARI=False
        if error==0 and ARI==False:
            with sqlite3.connect('DATABASEV1.db') as db:
                cursor=db.cursor()
                sql="INSERT INTO Trainers(Trainer_ID,Forename,Surname,Password,Phone,BEmail,DOB,Address,Sex) VALUES(?,?,?,?,?,?,?,?,?)"
                cursor.execute(sql,(self.Trainer_ID,Forename,Surname,Password,Phone,BEmail,DOB,Address,Sex))
                x=datetime.datetime.now()
                Date=x.strftime("%x")
                Time=x.strftime("%X")
                Reason="Sign Up"
                sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
                cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
                self.Email(BEmail)
                MessageBox = ctypes.windll.user32.MessageBoxW
                MessageBox(None, 'Welcome '+Forename+" "+Surname+" to SHIFT", 'Sign Up', )
                LoginPage.home(self)
        else:
            errorlist=Tk()
            errorlist.geometry('275x150')
            errorlist.overrideredirect(True)
            errorlist.after(3000,lambda Tk=errorlist:[Tk.destroy()])
            if error>0:
                error=str(error)
                errorl=Label(errorlist,text=error[0]+" out of 7 enteries do not meet the criteria",fg='red').place(x=25,y=25)
            elif ARI==True:
                errorlist=Label(errorlist,text="Trainer already in database",fg='red').place(x=25,y=25)
            elif error>0 and ARI==True:
                error=str(error)
                aril=Label(errorlist,text="Trainer already in database",fg='red').place(x=25,y=25)
                errorl=Label(errorlist,text=error[0]+" out of 6 enteries do not meet the criteria",fg='red').place(x=25,y=50)
    def Email(self,BEmail):
        __Gympass="Shiftgym10101"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",context=context) as server:
            server.login("shiftgymleisure@gmail.com", __Gympass)
            __sender_email = "shiftgymleisure@gmail.com"
            __receiver_email =BEmail
            __message = """\
                            Subject: Welcome 

                            
                                    Welcome to SHIFT Gym and Leisure centre
                                    You unique identification number is """+ str(self.Trainer_ID)+"""."""
            server.sendmail(__sender_email, __receiver_email, __message)

class HomePage ():
    def __init__(self,master,Trainer_ID):
        self.master=master
        self.Trainer_ID=Trainer_ID
        self.master.geometry('400x200')
        self.master.title("Home Page")
        self.wel=Label(self.master,text="Welcome",fg="green").place(x=175,y=25)
        self.client=Button(self.master,text="Clients",command=self.Client,width=12).place(x=100,y=100)
        self.trainers=Button(self.master,text="Trainers",command=self.Trainers,width=12).place(x=200,y=100)
        self.schedule=Button(self.master,text="Schedule",command=self.Schedule,width=12).place(x=150,y=65)
        self.sesh=Button(self.master,text="Sessions",command=self.Sessions,width=12).place(x=150,y=135)
        equipment=Button(self.master,text="Equipment",command=self.Equipment,width=12).place(x=5,y=170)
        switch=Button(self.master,text="Switch User",command=self.Switch,width=12).place(x=150,y=170)
        manager=Button(self.master,text="Manager Access",command=self.Manager,width=12).place(x=300,y=170)
    def Client(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            x=datetime.datetime.now()
            Date=x.strftime("%x")
            Time=x.strftime("%X")
            Reason="Acessing Client Table"
            sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
            cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
        call(["python", "Client.py"])
    def Trainers(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            x=datetime.datetime.now()
            Date=x.strftime("%x")
            Time=x.strftime("%X")
            Reason="Accessing Trainer Table"
            sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
            cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
        root6=Toplevel(self.master)
        myGui=TrainerPage(root6,self.Trainer_ID)
    def Schedule (self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            x=datetime.datetime.now()
            Date=x.strftime("%x")
            Time=x.strftime("%X")
            Reason="Accessing Schedule"
            sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
            cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
        root8=Toplevel(self.master)
        myGui=SchedulePage(root8,self.Trainer_ID)
    def Sessions (self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            x=datetime.datetime.now()
            Date=x.strftime("%x")
            Time=x.strftime("%X")
            Reason="Accessing Sessions"
            sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
            cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
        root5=Toplevel(self.master)
        myGui=SessionsPage(root5,self.Trainer_ID)
    def Switch(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            x=datetime.datetime.now()
            Date=x.strftime("%x")
            Time=x.strftime("%X")
            Reason="Sign Out"
            sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
            cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
        self.master.destroy()
    def Equipment(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            x=datetime.datetime.now()
            Date=x.strftime("%x")
            Time=x.strftime("%X")
            Reason="Accessing Equipment"
            sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
            cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
        root9=Toplevel(self.master)
        myGui=EquipmentPage(root9,self.Trainer_ID)
    def Manager(self):
        if int(self.Trainer_ID)==3000:
            with sqlite3.connect("DATABASEV1.db") as db:
                cursor=db.cursor()
                x=datetime.datetime.now()
                Date=x.strftime("%x")
                Time=x.strftime("%X")
                Reason="Manager Access"
                sql="INSERT INTO Log(Trainer_ID,Date,Time,Reason)VALUES(?,?,?,?)"
                cursor.execute(sql,(self.Trainer_ID,Date,Time,Reason))
            root10=Toplevel(self.master)
            myGui=ManagerPage(root10,self.Trainer_ID)

class SessionsPage():
    def __init__(self,master,Trainer_ID):
        self.master=master
        self.Trainer_ID=Trainer_ID
        self.master.title('Sessions')
        self.master.geometry('500x250')
        self.sesh = StringVar()
        self.sesht=StringVar()
        self.SID=StringVar()
        self.CID=StringVar()
        self.date=StringVar()
        self.time=StringVar()
        self.duration=StringVar()
        self.studio=StringVar()
        self.equipment=StringVar()
        self.equcount=0
        self.flist=[]
        self.clientlist=[]
        self.times=[0.3,1.0,1.3,2.0,2.3]
        seshtype=["1:1","Class"]
        self.sesht.set("Choose Type Of Session")
        sesht = OptionMenu(self.master,self.sesht, *seshtype,command=self.Sessiontype).place(x=165,y=30)
        self.save=Button(self.master,text="Save")
        self.save.place(x=140,y=200)
        self.exit=Button(self.master,text="Exit",command=self.Exit).place(x=240,y=200)
        self.delete=Button(self.master,text="Delete",command=self.Delete).place(x=340,y=200)
        cidl=Label(self.master,text="ClientID(s)",fg="black").place(x=50,y=80)
        self.cid=Entry(self.master,textvariable=self.CID,width=15,state='disabled')
        self.cid.place(x=50,y=100)
        datl=Label(self.master,text="Date:").place(x=150,y=80)
        self.dat=Entry(self.master,textvariable=self.date,width=15,state='disabled',bg='white')
        self.dat.place(x=150,y=100)
        timl=Label(self.master,text="Time(hh.mm):").place(x=250,y=80)
        self.tim=Entry(self.master,textvariable=self.time,width=15).place(x=250,y=100)
        durl=Label(self.master,text="Duration(hh.mm):").place(x=350,y=80)
        self.dur=OptionMenu(self.master,self.duration, *self.times).place(x=350,y=100)
        stul=Label(self.master,text="Studio(Y|N):").place(x=150,y=121)
        self.stu=Entry(self.master,textvariable=self.studio,width=15).place(x=150,y=140)
        eql=Label(self.master,text="Equipment:").place(x=250,y=121)
        self.equ=Entry(self.master,textvariable=self.equipment,width=15,state='disabled')
        self.equ.place(x=250,y=140)
        self.dat.bind('<1>',self.Calpop)
        self.equ.bind('<1>',self.Equpop)
        self.cid.bind('<1>',self.Clipop)
    
    def Exit(self):
        self.master.destroy()
    
    def Delete(self):
        SessionID=self.SID.get()
        type=self.sesht.get()
        if type=="Class":
            with sqlite3.connect("DATABASEV1.db") as db:
                cursor=db.cursor()
                cer="SELECT CReservationID, EReservationID FROM Class WHERE ClassID=?"
                cursor.execute(cer,(SessionID,))
                cer=cursor.fetchall()
                dele="DELETE FROM Class WHERE ClassID=?"
                cursor.execute(dele,(SessionID,))
                hold= pd.read_excel(cer[0][1]+'.xlsx')
                equipid=list(hold[0])
                upe="UPDATE Equipment SET Reserved=Reserved-1 WHERE EquipmentID=?"
                for x in range(len(equipid)):
                    cursor.execute(upe,(str(equipid[x]),))
                os.remove(cer[0][1]+".xlsx")
                os.remove(str(cer[0][0])+".xlsx")
                try:
                    name=str(SessionID)+str(self.Trainer_ID)
                    os.remove(name+".xlsx")
                except:
                    pass  
                sql3="SELECT EquipmentID FROM Equipment"
                cursor.execute(sql3,())
                id=cursor.fetchall()
                for x in range(len(id)):
                    que=Queue()
                    name=str(id[x][0])
                    try:
                        Queue.Retrieve(que,name)
                        que.queue.remove(id[x][0])
                    except:
                        pass
                Queue.Save(que,name) 
        elif type=="1:1":
            with sqlite3.connect("DATABASEV1.db") as db:
                cursor=db.cursor()
                cer="SELECT EReservationID FROM Session WHERE SeshID=?"
                cursor.execute(cer,(SessionID,))
                cer=cursor.fetchall()
                dele="DELETE FROM Session WHERE SeshID=?"
                cursor.execute(dele,(SessionID,))
                hold= pd.read_excel(cer[0][0]+'.xlsx')
                equipid=list(hold[0])
                upe="UPDATE Equipment SET Reserved=Reserved-1 WHERE EquipmentID=?"
                for x in range(len(equipid)):
                    cursor.execute(upe,(str(equipid[x]),))
                os.remove(cer[0][0]+".xlsx")
                sql3="SELECT EquipmentID FROM Equipment"
                cursor.execute(sql3,())
                id=cursor.fetchall()
                for x in range(len(id)):
                    que=Queue()
                    name=str(id[x][0])
                    try:
                        Queue.Retrieve(que,name)
                        que.queue.remove(id[x][0])
                    except:
                        pass
                Queue.Save(que,name) 
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Session deleted', 'Session', ) 
    
    def Calpop(self,pop):
        calroot=Tk()
        calroot.title("Session Date")
        x=datetime.datetime.now()
        day=x.strftime("%d")
        month=x.strftime("%m")
        year=x.strftime("%Y")
        cal = Calendar(calroot,font="Arial 14", selectmode='day',date_pattern='dd/mm/yy',cursor="hand1",background='Black',foreground='Orange', year=int(year), month=int(month), day=int(day))
        cal.pack(fill="both")
        def done():
            caldate=cal.get_date()
            self.date.set(caldate)
            calroot.destroy()
        but=Button(calroot,text="Enter Date",command=done,width=15)
        but.pack(fill="x")
    
    def Equpop(self,event):
        equroot=Tk()
        equroot.title("Session Equipment")
        self.flist=[]
        def dOne():
            for i in equip.curselection():
                self.equcount=self.equcount+1
                equipment=equip.get(i)
                self.flist.append(equipment[0])
            if self.sesh.get()=="Add New Session":
                self.equipment.set("Selected")
            equroot.destroy()
        with sqlite3.connect ("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT EquipmentID,Name FROM Equipment"
            cursor.execute(sql)
            equipmentlist=list(cursor.fetchall())
        equip=Listbox(equroot,height=10,selectmode='multiple')
        equip.pack(fill="both")
        save=Button(equroot,text="Enter Equipment",command=dOne,width=12)
        save.pack(fill="both")
        for item in equipmentlist:
                equip.insert(END,item)
    
    def SavePre(self):
        SessionID=self.SID.get()
        Duration=self.duration.get()
        Studio=self.studio.get()
        EReservationID=self.equipment.get()
        CReservationID=self.CID.get()
        Date=self.date.get()
        Time=self.time.get()
        error=False
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            DTsql="SELECT Date,Time,Duration FROM Session WHERE Trainer_ID=? AND SeshID!=?"
            cursor.execute(DTsql,(self.Trainer_ID,SessionID,))
            DT=cursor.fetchall()
        for x in range(len(DT)):
            if error==True:
                error=True
            elif Date==DT[x][0] and (float(DT[x][1])<=float(Time)<float(DT[x][1])+float(DT[x][2]) or float(DT[x][1])<float(Time)+float(Duration)<=float(DT[x][1])+float(DT[x][2])):
                error=True
            else:
                error=False
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            DTsql="SELECT Date,Time,Duration FROM Class WHERE Trainer_ID=? AND ClassID!=?"
            cursor.execute(DTsql,(self.Trainer_ID,SessionID))
            DT=cursor.fetchall()
        for x in range(len(DT)):
            if error==True:
                error=True
            elif Date==DT[x][0] and (float(DT[x][1])<=float(Time)<float(DT[x][1])+float(DT[x][2]) or float(DT[x][1])<float(Time)+float(Duration)<=float(DT[x][1])+float(DT[x][2])):
                error=True
            else:
                error=False
        if error==False:
            Cel=len(self.flist)
            print(Cel)
            if Cel>=1:
                currentequ=self.flist
                ndb=[]
                hold= pd.read_excel(EReservationID+'.xlsx')
                dbequip=list(hold[0])
                for x in range(len(dbequip)):
                    if str(dbequip[x]) in currentequ:
                        currentequ.remove(dbequip[x])
                    elif  str(dbequip[x]) not in currentequ: 
                        ndb.append(dbequip[x])
                for x in range(len(ndb)):
                    dbequip.remove(ndb[x])
                if len(ndb)!=0:
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        for x in range(len(ndb)):
                            ree="UPDATE Equipment SET Reserved=Reserved-1 WHERE EquipmentID=?"
                            cursor.execute(ree,(ndb[x],))
                instock=[]
                nstock=[]
                with sqlite3.connect("DATABASEV1.db") as connection:
                    cursor=connection.cursor()
                    cesql="SELECT Reserved,Stock FROM Equipment WHERE EquipmentID=?"
                    for x in range(len(currentequ)):
                        cursor.execute(cesql,(currentequ[x],))
                        rs=cursor.fetchall()
                        if rs[0][0]<rs[0][1]:
                            instock.append(currentequ[x])
                        elif rs[0][0]==rs[0][1]:
                            nstock.append(currentequ[x])
                currentequ.extend(dbequip)
                for z in range(len(nstock)):
                    eque=Queue()
                    Queue.Enqueue(eque,SessionID)
                    name=str(nstock[z])
                    Queue.Save(eque,name)
            type=self.sesht.get()
            ccl=len(self.clientlist)
            if type=="1:1":
                if ccl==1:
                    ClientID=self.clientlist[0]
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        fsql="UPDATE Session SET ClientID=?,Date=?,Time=?,Duration=?,Studio=? WHERE SeshID=?"
                        cursor.execute(fsql,(ClientID,Date,Time,Duration,Studio,SessionID))
                        if Cel>=1:
                            fequ="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                            for x in range(len(instock)):
                                cursor.execute(fequ,(instock[x],))
                            df = pd.DataFrame(currentequ)
                            writer = pd.ExcelWriter(EReservationID+'.xlsx', engine='xlsxwriter')
                            df.to_excel(writer, sheet_name='welcome', index=False)
                            writer.save()
                elif ccl==0:
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        fsql="UPDATE Session SET Date=?,Time=?,Duration=?,Studio=? WHERE SeshID=?"
                        cursor.execute(fsql,(Date,Time,Duration,Studio,SessionID))
                        if Cel>0:
                            df = pd.DataFrame(currentequ)
                            writer = pd.ExcelWriter(EReservationID+'.xlsx', engine='xlsxwriter')
                            df.to_excel(writer, sheet_name='welcome', index=False)
                            writer.save()
                            fequ="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                            for x in range(len(instock)):
                                cursor.execute(fequ,(instock[x],)) 
                                 
            elif type=="Class":
                ndb=[]
                if ccl==0:
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        fsql="UPDATE Class SET Date=?,Time=?,Duration=?,Studio=? WHERE ClassID=?"
                        cursor.execute(fsql,(Date,Time,Duration,Studio,SessionID))
                        if Cel>0:
                            fequ="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                            for x in range(len(instock)):
                                cursor.execute(fequ,(instock[x],)) 
                            df = pd.DataFrame(currentequ)
                            writer = pd.ExcelWriter(EReservationID+'.xlsx', engine='xlsxwriter')
                            df.to_excel(writer, sheet_name='welcome', index=False)
                            writer.save()    
                elif ccl>0 and ccl<=5:
                    currentcli=self.clientlist
                    aclass=[]
                    hold= pd.read_excel(CReservationID+'.xlsx')
                    dbclient=list(hold[0])
                    for x in range(len(dbclient)):
                        if str(dbclient[x]) in currentcli:
                            currentcli.remove(dbclient[x])
                            aclass.append(dbclient[x])
                        elif  str(dbclient[x]) not in currentcli: 
                            ndb.append(dbclient[x])
                    aclass.extend(currentcli)
                    if len(aclass)>5:
                        que=Queue()
                        name=str(SessionID)+str(self.Trainer_ID)
                        Queue.Retrieve(que,name)
                        for x in range(5-len(aclass)):
                            currentcli.append(que.queue[x])
                        for x in range(len(que.queue)):
                            if que.queue[x] in currentcli:
                                Queue.Dequeue(que)
                        Queue.Save(que,name)
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        fsql="UPDATE Class SET Date=?,Time=?,Duration=?,Studio=? WHERE ClassID=?"
                        cursor.execute(fsql,(Date,Time,Duration,Studio,SessionID))
                        df = pd.DataFrame(aclass)
                        writer = pd.ExcelWriter(CReservationID+'.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='welcome', index=False)
                        writer.save()
                        if Cel>0:
                            df = pd.DataFrame(currentequ)
                            writer = pd.ExcelWriter(EReservationID+'.xlsx', engine='xlsxwriter')
                            df.to_excel(writer, sheet_name='welcome', index=False)
                            writer.save()
                            fequ="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                            for x in range(len(instock)):
                                cursor.execute(fequ,(instock[x],))  
                
                elif ccl<5:
                    currentcli=self.clientlist
                    nclass=[]
                    inclass=[]
                    for x in range(5):
                        inclass.append(currentcli[x])
                    nclass.extend(currentcli[6:])
                    hold= pd.read_excel(CReservationID+'.xlsx')
                    dbclient=list(hold[0])
                    for x in range(len(dbclient)):
                        if str(dbclient[x][0]) in inclass:
                            inclass.remove(dbclient[x][0])
                        elif  str(dbclient[x][0]) not in inclass: 
                            ndb.append(dbclient[x][0])
                    que=Queue()
                    name=str(SessionID)+str(self.Trainer_ID)
                    Queue.Retrieve(que,name)
                    for x in range(len(nclass)):
                        if len(nclass)>10:
                        #the first 10 will be enqueued to the queue
                            for z in range(10):
                                x=str(nclass[0])
                                nclass.pop(0)
                                Queue.Enqueue(que,x)
                        #lets trainer know 10 out of the remaing clients are put in the queue but the remainder are not
                    #if length of clients is less than or equal to the max number of queue space
                        elif len(nclass)<=10:
                            for z in range(len(nclass)):
                                x=str(nclass[z])
                                Queue.Enqueue(que,x)
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        fsql="UPDATE Class SET Date=?,Time=?,Duration=?,Studio=? WHERE ClassID=?"
                        cursor.execute(fsql,(Date,Time,Duration,Studio,SessionID))
                        if Cel>0:
                            fequ="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                            for x in range(len(instock)):
                                cursor.execute(fequ,(instock[x],))  
                        df = pd.DataFrame(currentequ)
                        writer = pd.ExcelWriter(EReservationID+'.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='welcome', index=False)
                        writer.save()
                        df = pd.DataFrame(inclass)
                        writer = pd.ExcelWriter(CReservationID+'.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='welcome', index=False)
                        writer.save()
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Session updated', 'Session', )            
        elif error==True:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'You already have a session at this time choose another or it collides with another', 'Session', )  
            M2essageBox = ctypes.windll.user32.MessageBoxW
            M2essageBox(None, "Avoid theses Dates and Times "+str(DT), 'Session', )  
                       
    def SaveNew(self):
        SessionID=self.SID.get()
        Duration=self.duration.get()
        Studio=self.studio.get()
        Date=self.date.get()
        Time=self.time.get()
        error=False
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            DTsql="SELECT Date,Time,Duration FROM Session WHERE Trainer_ID=?"
            cursor.execute(DTsql,(self.Trainer_ID,))
            DT=cursor.fetchall()
        for x in range(len(DT)):
            if error==True:
                error=True
            elif Date==DT[x][0] and (float(DT[x][1])<=float(Time)<float(DT[x][1])+float(DT[x][2]) or float(DT[x][1])<float(Time)+float(Duration)<=float(DT[x][1])+float(DT[x][2])):
                error=True
            else:
                error=False
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            DTsql="SELECT Date,Time,Duration FROM Class WHERE Trainer_ID=?"
            cursor.execute(DTsql,(self.Trainer_ID,))
            DT=cursor.fetchall()
        for x in range(len(DT)):
            if error==True:
                error=True
            elif Date==DT[x][0] and (float(DT[x][1])<=float(Time)<float(DT[x][1])+float(DT[x][2]) or float(DT[x][1])<float(Time)+float(Duration)<=float(DT[x][1])+float(DT[x][2])):
                error=True
            else:
                error=False
        if error==False:   
            Equipment=self.flist
            Instock=[]
            Nstock=[]
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                Esql="SELECT Reserved,Stock FROM Equipment WHERE EquipmentID=? "
                for x in range(len(Equipment)):
                    cursor.execute(Esql,(Equipment[x],))
                    Estock=cursor.fetchall()
                    if int(Estock[0][0])<int(Estock[0][1]):
                        Instock.append(Equipment[x])
                    elif int(Estock[0][0])==int(Estock[0][1]):
                        Nstock.append(Equipment[x])
            for z in range(len(Nstock)):
                eque=Queue()
                name=str(Nstock[z])
                try:
                    Queue.Retrieve(eque,name)
                except:
                    pass
                Queue.Enqueue(eque,SessionID)
                Queue.Save(eque,name)
            EquipmentC=len(Instock)
            id=[]
            id2=[]
            for x in range(3):
                letter=random.choice(string.ascii_letters) 
                id.append(letter)
            REquipmentID = "".join(id)
            for x in range(4):
                letter2=random.choice(string.ascii_letters) 
                id2.append(letter2)
            RClientID = "".join(id2)
            Clients=self.clientlist
            Type=self.sesht.get()
            if Type=="Class":
                SessionID=random.randint(5000,5999)
                Current=len(Clients)
                Max=5
                if Current<Max or Current==Max:
                    #Send everything off
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        sql="INSERT INTO Class(ClassID,Trainer_ID,CReservationID,EReservationID,Date,Time,Duration,Studio,Current,Max) VALUES(?,?,?,?,?,?,?,?,?,?)"
                        cursor.execute(sql,(SessionID,self.Trainer_ID,RClientID,REquipmentID,Date,Time,Duration,Studio,Current,Max))
                        sql2="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                        for x in range(EquipmentC):
                            EquipmentID=Instock[x]
                            cursor.execute(sql2,(EquipmentID,))
                        df = pd.DataFrame(Clients)
                        writer = pd.ExcelWriter(RClientID+'.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='welcome', index=False)
                        writer.save()
                        df = pd.DataFrame(Instock)
                        writer = pd.ExcelWriter(REquipmentID+'.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='welcome', index=False)
                        writer.save()
                        que=Queue()
                        name=str(SessionID)+str(self.Trainer_ID)
                        Queue.Save(que,name)
                elif Current>Max:
                    #Creates list that will hold 5 clients
                    Inclass=[]
                    for x in range(5):
                        #Moves First 5 ClientIDs To Inclass and Removes Them From Clients
                        Inclass.append(Clients[0])
                        Clients.pop(0)
                    #Sets Current To Equal Max
                    Current=5
                    #Moves Remaining IDs to Queue
                    que=Queue()
                    #if length of clients go over the max number of queue space
                    if len(Clients)>10:
                        #the first 10 will be enqueued to the queue
                        for z in range(10):
                            x=str(Clients[0])
                            Clients.pop(0)
                            Queue.Enqueue(que,x)
                        #lets trainer know 10 out of the remaing clients are put in the queue but the remainder are not
                    #if length of clients is less than or equal to the max number of queue space
                    elif len(Clients)<=10:
                        for z in range(len(Clients)):
                            x=str(Clients[z])
                            Queue.Enqueue(que,x)
                    #Saves the queue to an excel file uniquley created and identifiable via the combonation of session id and trainer id
                    name=str(SessionID)+str(self.Trainer_ID)
                    Queue.Save(que,name)
                    #Send everything off
                    with sqlite3.connect("DATABASEV1.db") as db:
                        cursor=db.cursor()
                        sql="INSERT INTO Class(ClassID,Trainer_ID,CReservationID,EReservationID,Date,Time,Duration,Studio,Current,Max) VALUES(?,?,?,?,?,?,?,?,?,?)"
                        cursor.execute(sql,(SessionID,self.Trainer_ID,RClientID,REquipmentID,Date,Time,Duration,Studio,Current,Max))
                        sql2="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                        for x in range(EquipmentC):
                            EquipmentID=Instock[x]
                            cursor.execute(sql2,(EquipmentID,))
                        df = pd.DataFrame(Inclass)
                        writer = pd.ExcelWriter(RClientID+'.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='welcome', index=False)
                        writer.save()
                        df = pd.DataFrame(Instock)
                        writer = pd.ExcelWriter(REquipmentID+'.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, sheet_name='welcome', index=False)
                        writer.save()
            elif Type=="1:1":
                #Sends Everything Off
                SessionID=random.randint(4000,4999)
                with sqlite3.connect("DATABASEV1.db") as db:
                    cursor=db.cursor()
                    sql="INSERT INTO Session(SeshID,Trainer_ID,ClientID,EReservationID,Date,Time,Duration,Studio) VALUES(?,?,?,?,?,?,?,?)"
                    cursor.execute(sql,(SessionID,self.Trainer_ID,Clients[0],REquipmentID,Date,Time,Duration,Studio))
                    sql2="UPDATE Equipment SET Reserved=Reserved+1 WHERE EquipmentID=?"
                    for x in range(EquipmentC):
                        EquipmentID=Instock[x]
                        cursor.execute(sql2,(EquipmentID,))
                    df = pd.DataFrame(Instock)
                    writer = pd.ExcelWriter(REquipmentID+'.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='welcome', index=False)
                    writer.save()
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Session added', 'Session', )            
        elif error==True:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'You already have a session at this time choose another or it collides with another', 'Session', )  
            M2essageBox = ctypes.windll.user32.MessageBoxW
            M2essageBox(None, "Avoid theses Dates and Times "+str(DT), 'Session', )  
            
    def Sessionpull(self,click):
        choice=self.sesh.get()
        num=self.num
        if choice=="Add New Session" :
                self.CID.set("")
                self.date.set("")
                self.time.set("")
                self.duration.set("")
                self.studio.set("")
                self.equipment.set("")
                self.save.config(command=self.SaveNew)
        else:
            for y in range(num):
                if choice[2:10]==self.x[y][4] and choice[14:19]==self.x[y][5]:
                    self.SID.set(self.x[y][0])
                    self.CID.set(self.x[y][2])
                    self.date.set(self.x[y][4])
                    self.time.set(self.x[y][5])
                    self.duration.set(self.x[y][6])
                    self.studio.set(self.x[y][7])
                    self.equipment.set(self.x[y][3])
                    self.save.config(command=self.SavePre)
            
    def Clipop(self,event):
        self.clientlist=[]
        clientroot=Tk()
        clientroot.title("Session Clients")        
        def dOne():
            for i in equip.curselection():
                Fclient=equip.get(i)
                self.clientlist.append(Fclient[0])
            if self.sesh.get()=="Add New Session":
                self.CID.set("Selected")
            clientroot.destroy()
        with sqlite3.connect ("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT ClientID,Surname,Forename FROM Clients WHERE Trainer_ID=?"
            cursor.execute(sql,(self.Trainer_ID,))
            equipmentlist=list(cursor.fetchall())
        if self.sesht.get()=="Class":
            equip=Listbox(clientroot,height=10,selectmode='multiple')
            equip.pack(fill="both")
        else:
            equip=Listbox(clientroot,height=10)
            equip.pack(fill="both")
        save=Button(clientroot,text="Enter Clients",command=dOne,width=12)
        save.pack(fill="both")
        for item in equipmentlist:
                equip.insert(END,item)
        
    def Sessiontype(self,click):
        type=self.sesht.get()
        self.sessions=[]
        if type=="1:1":
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT COUNT(SeshID) FROM Session WHERE Trainer_ID=?"
                try:
                    cursor.execute(sql,(self.Trainer_ID,))
                    self.num=((cursor.fetchall()[0][0]))
                except:
                    self.num=0
                sql2="SELECT * from Session WHERE Trainer_ID=? "
                cursor.execute(sql2,(self.Trainer_ID,))
                self.x=cursor.fetchall()
            for y in range(self.num):
                self.sessions.append(self.x[y][4:6])
            self.sessions.append("Add New Session")
            self.sesh.set("Choose A Session")
            sesh = OptionMenu(self.master,self.sesh, *self.sessions,command=self.Sessionpull).place(x=250,y=30)
            self.CID.set("")
            self.date.set("")
            self.time.set("")
            self.duration.set("")
            self.studio.set("")
            self.equipment.set("")
        elif type=="Class":
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT COUNT(ClassID) FROM Class WHERE Trainer_ID=? "
                cursor.execute(sql,(self.Trainer_ID,))
                try:
                    cursor.execute(sql,(self.Trainer_ID,))
                    self.num=((cursor.fetchall()[0][0]))
                except:
                    self.num=0
                sql2="SELECT * from Class WHERE Trainer_ID=? "
                cursor.execute(sql2,(self.Trainer_ID,))
                self.x=cursor.fetchall()
            if len(self.x)!=0:
                for y in range(self.num):
                    self.sessions.append(self.x[y][4:6])
            self.sessions.append("Add New Session")
            self.sesh.set("Choose A Session")
            sesh = OptionMenu(self.master,self.sesh, *self.sessions,command=self.Sessionpull).place(x=250,y=30)
            self.CID.set("")
            self.date.set("")
            self.time.set("")
            self.duration.set("")
            self.studio.set("")
            self.equipment.set("")

class TrainerPage():
    def __init__(self,master,Trainer_ID):
        self.master=master
        self.Trainer_ID=Trainer_ID
        self.master.geometry('400x300')
        self.master.title('Trainer')
        self.sur=StringVar()
        self.fore=StringVar()
        self.password=StringVar()
        self.phone=StringVar()
        self.address=StringVar()
        self.email=StringVar()
        self.dob=StringVar()
        self.sex=StringVar()
        with  sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT * FROM Trainers WHERE Trainer_ID=?"
            cursor.execute(sql,(Trainer_ID,))
            data=list(cursor.fetchall())
            info=data[0]
        self.sur.set(info[2])
        self.fore.set(info[1])
        self.password.set(info[3])
        self.phone.set(info[4])
        self.address.set(info[7])
        self.email.set(info[5])
        self.dob.set(info[6])
        self.sex.set(info[8])
        self.forel=Label(self.master,text="Forename:",fg='black',width=12).place(x=15,y=25)        
        self.surl=Label(self.master,text="Surname:",fg='black',width=12).place(x=18,y=50)
        self.passl=Label(self.master,text="Password:",fg='black',width=12).place(x=18,y=75)
        self.phol=Label(self.master,text="Phone:",fg='black',width=12).place(x=25,y=100)
        self.emal=Label(self.master,text="Email:",fg='black',width=12).place(x=175,y=25)
        self.dobl=Label(self.master,text="DOB:",fg='black',width=12).place(x=178,y=50)
        self.adrl=Label(self.master,text="Address:",fg='black',width=12).place(x=170,y=75)
        self.sexl=Label(self.master,text="Sex:",fg='black',width=12).place(x=181,y=101)
        self.tral=Label(self.master,text="Trainer ID: "+str(info[0]),width=30).place(x=110,y=130)
        self.forebx=Entry(self.master,textvariable=self.fore,width=12).place(x=90,y=28)
        self.surbx=Entry(self.master,textvariable=self.sur,width=12).place(x=90,y=53)
        self.passbx=Entry(self.master,textvariable=self.password,width=12).place(x=90,y=78)
        self.phobx=Entry(self.master,textvariable=self.phone,width=12).place(x=90,y=103)
        self.emabx=Entry(self.master,textvariable=self.email,width=12).place(x=238,y=27)
        dobbx = DateEntry(self.master,textvariable=self.dob,day=int(info[6][0:2]),month=int(info[6][3:5]),year=int(info[6][6:8]),date_pattern='dd/mm/yy', width=12, background='black',foreground='Orange',).place(x=238,y=53)
        self.adrbx=Entry(self.master,textvariable=self.address,width=12).place(x=238,y=77)
        self.sexbx=Entry(self.master,textvariable=self.sex,width=12).place(x=238,y=104)
        self.back=Button(self.master,text="Back",command=self.Close,width=15).place(x=80,y=165)
        self.edit=Button(self.master,text="Edit",command=self.Update,width=15).place(x=230,y=165)
        self.other=Button(self.master,text="Trainers",command=self.Access,width=15).place(x=150,y=200)
    def Close(self):
        self.master.destroy()
    def Update(self):
        Forename=self.fore.get()
        Surname=self.sur.get()
        Password=self.password.get()
        Phone=self.phone.get()
        Email=self.email.get()
        DOB=self.dob.get()
        Address=self.address.get()
        Sex=self.sex.get()
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            sql="UPDATE Trainers SET Forename=?,Surname=?,Password=?,Phone=?,BEmail=?,DOB=?,Address=?,Sex=? WHERE Trainer_ID=?"
            cursor.execute(sql,(Forename,Surname,Password,Phone,Email,DOB,Address,Sex,self.Trainer_ID,))
    def Access(self):
        roo2t=Toplevel()
        myGUIWelcome=AccessTrainers(roo2t,self.Trainer_ID)

class AccessTrainers():
    def __init__(self,master,Trainer_ID):
        self.master=master
        self.Trainer_ID=Trainer_ID
        self.master.geometry('400x150')
        self.master.title('Trainers')
        self.choosen=StringVar()
        self.fname=StringVar()
        self.lname=StringVar()
        self.bemail=StringVar()
        self.sex=StringVar()
        self.dob=StringVar()
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT * FROM Trainers WHERE Trainer_ID!=?"
            cursor.execute(sql,(self.Trainer_ID,))
            trainers=cursor.fetchall()
            self.trainerlist=[]
            for x in range(len(trainers)):
                self.trainerlist.append(trainers[x][0:3])
            self.trainerchoose=ttk.Combobox(self.master,textvariable=self.choosen,values=self.trainerlist,width=50)
            self.trainerchoose.pack()
            fnl=Label(self.master,text="Forename:",fg='black').place(x=40,y=30)
            lnl=Label(self.master,text="Surname:",fg='black').place(x=150,y=30)
            bel=Label(self.master,text="BEmail",fg='black').place(x=280,y=30)
            sel=Label(self.master,text="Sex:").place(x=40,y=80)
            dol=Label(self.master,text="DOB:").place(x=280,y=80)
            forebx=Entry(self.master,textvariable=self.fname,width=12,state='disable').place(x=40,y=50)
            surbx=Entry(self.master,textvariable=self.lname,width=12,state='disable').place(x=160,y=50)
            bemail=Entry(self.master,textvariable=self.bemail,width=12,state='disable').place(x=280,y=50)
            sex=Entry(self.master,textvariable=self.sex,width=12,state='disable').place(x=40,y=100)
            dob=Entry(self.master,textvariable=self.dob,width=12,state='disable').place(x=280,y=100)
            Button(self.master,text="Exit",command=lambda Tk=self.master:[Tk.destroy()],width=12).place(x=160,y=100)
            self.trainerchoose.bind('<KeyRelease>',self.Gthread)
            self.trainerchoose.bind('<<ComboboxSelected>>',self.Print)
    def Gthread(self,event):
        gthread=Thread(target=self.GoogleRipOff)
        gthread.start()
    def GoogleRipOff(self):
        cholen=int(len(self.choosen.get()))
        chosen=self.choosen.get()
        if cholen!=0:
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT Trainer_ID, Forename, Surname FROM Trainers WHERE Trainer_ID!=? AND SUBSTR(Forename, 1, ?) = ?  OR SUBSTR(Surname, 1, ?) = ? ORDER BY Trainer_ID"
                cursor.execute(sql,(self.Trainer_ID,cholen,chosen,cholen,chosen,))
                new=cursor.fetchall()
                self.trainerlist.clear()
                self.trainerlist=new
        elif cholen==0:
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT * FROM Trainers WHERE Trainer_ID!=?"
                cursor.execute(sql,(self.Trainer_ID,))
                trainers=cursor.fetchall()
                self.trainerlist=[]
            for x in range(len(trainers)):
                self.trainerlist.append(trainers[x][0:3])
        self.trainerchoose.config(values=self.trainerlist)
    def Print(self,event):
        choosen=self.choosen.get()
        Trainer_ID=choosen[0:5]
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT Forename,Surname,BEmail,Sex,DOB FROM Trainers WHERE Trainer_ID=?"
            cursor.execute(sql,(Trainer_ID,))
            tinfo=cursor.fetchall()
            
        self.fname.set(tinfo[0][0])
        self.lname.set(tinfo[0][1])
        self.bemail.set(tinfo[0][2])
        self.sex.set(tinfo[0][3])
        self.dob.set(tinfo[0][4])

class SchedulePage():
    def __init__(self,master,Trainer_ID):
        self.master=master
        self.Trainer_ID=Trainer_ID
        self.master.title("Schedule Page")
        self.master.geometry('500x464')
        search=["All","Class","1:1",self.Trainer_ID+" All",self.Trainer_ID+" Class",self.Trainer_ID+" 1:1"]
        self.search=StringVar()
        self.tdt=StringVar()
        self.search.set(search[0])
        self.cal = Calendar(self.master,font="Arial 14", selectmode='day',date_pattern='dd/mm/yy',cursor="hand1",background='Black',foreground='Orange')
        self.cal.pack(fill="x")
        searcht = OptionMenu(self.master,self.search,*search,command=self.Editlistbox).pack(fill="x")
        self.Editlistbox(self.search)
        self.fsearch=Listbox(self.master,selectmode=BROWSE,listvariable=self.tdt,)
        self.fsearch.pack(fill="both")
        Button(self.master,text="Exit",command=lambda Tk=self.master:[Tk.destroy()]).pack(fill="both")
        self.cal.bind('<<CalendarSelected>>',self.Editlistbox)
        self.fsearch.bind('<<ListboxSelect>>',self.Grab)
        
    def Grab(self,click):
        self.celist=StringVar()
        here=self.fsearch.curselection()
        popup=self.dbtdt[here[0]]
        self.ce=StringVar()
        if int(popup[0])>=4000 and int(popup[0])<=4999:
            sql="SELECT Session.*, Trainers.Forename,Trainers.Surname FROM Session INNER JOIN Trainers ON Session.Trainer_ID = Trainers.Trainer_ID WHERE SeshID=?"
        elif int(popup[0])>=5000 and int(popup[0])<=5999:
            sql="SELECT Class.*, Trainers.Forename,Trainers.Surname FROM Class INNER JOIN Trainers ON Class.Trainer_ID = Trainers.Trainer_ID WHERE ClassID=?"
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            cursor.execute(sql,(popup[0],))
            self.pudata=cursor.fetchall()
        Popup=Toplevel()
        Popup.title("Session "+str(popup[0]))
        Popup.geometry('400x250')
        try:
            types="Class"
            Label(Popup,text="SessionID:"+str(self.pudata[0][0])).place(x=50,y=15)
            Label(Popup,text="Trainer:"+self.pudata[0][10]+" "+self.pudata[0][11]).place(x=50,y=30)
            Label(Popup,text="Client(s):"+self.pudata[0][2]).place(x=50,y=45)
            Label(Popup,text="Equipment:"+self.pudata[0][3]).place(x=50,y=60)
            Label(Popup,text="Type:"+types,).place(x=50,y=75)
            Label(Popup,text="Date:"+self.pudata[0][4]).place(x=50,y=90)
            Label(Popup,text="Time:"+self.pudata[0][5]).place(x=50,y=105)
            Label(Popup,text="Duration:"+self.pudata[0][6]).place(x=50,y=120)
            Label(Popup,text="Studio:"+self.pudata[0][7]).place(x=50,y=135)
        except:
            types="1:1"
            Label(Popup,text="SessionID:"+str(self.pudata[0][0])).place(x=50,y=15)
            Label(Popup,text="Trainer:"+self.pudata[0][8]+" "+self.pudata[0][9]).place(x=50,y=30)
            Label(Popup,text="Client(s):"+str(self.pudata[0][2])).place(x=50,y=45)
            Label(Popup,text="Equipment:"+self.pudata[0][3]).place(x=50,y=60)
            Label(Popup,text="Type:"+types,).place(x=50,y=75)
            Label(Popup,text="Date:"+self.pudata[0][4]).place(x=50,y=90)
            Label(Popup,text="Time:"+self.pudata[0][5]).place(x=50,y=105)
            Label(Popup,text="Duration:"+self.pudata[0][6]).place(x=50,y=120)
            Label(Popup,text="Studio:"+self.pudata[0][7]).place(x=50,y=135)
        self.list=Listbox(Popup,listvariable=self.celist,).place(x=260,y=15)
        equb=Button(Popup,text="Equipment Reserved",command=self.Pullequ).place(x=50,y=135)
        clib=Button(Popup,text="   Client List   ",command=self.Pullcli,width=15).place(x=50,y=165)
        Button(Popup,text="Exit",command=lambda Tk=Popup:[Tk.destroy()]).place(x=350,y=195)
        Button(Popup,text="View Queue",command=self.Pullque,width=15).place(x=50,y=195)
    
    def Pullequ(self):
        self.ce=[]
        en=[]
        hold= pd.read_excel(self.pudata[0][3]+'.xlsx')
        hold=list(hold[0])
        for x in range (len(hold)):
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT EquipmentID, Name FROM Equipment WHERE EquipmentID=?"
                cursor.execute(sql,(str(hold[x]),))
                egrab=cursor.fetchall()
                en.append(egrab[0])
        for x in range(len(en)):
                en2=str(en[x][0]),en[x][1]
                self.ce.append(en2)
        self.celist.set(self.ce)
         
    def Pullcli(self):
        self.ce=[]
        en=[]
        try:
            hold= pd.read_excel(self.pudata[0][2]+'.xlsx')
            hold=list(hold[0])
            for x in range (len(hold)):
                with sqlite3.connect("DATABASEV1.db") as connection:
                    cursor=connection.cursor()
                    sql="SELECT ClientID,Forename,Surname  FROM Clients WHERE ClientID=?"
                    cursor.execute(sql,(str(hold[x]),))
                    egrab=cursor.fetchall()
                    en.append(egrab[0])
            for x in range(len(en)):
                    en2=str(en[x][0]),en[x][1],en[x][2]
                    self.ce.append(en2)
            self.celist.set(self.ce)
        except:
            with sqlite3.connect("DATABASEV1.db") as connection:
                    cursor=connection.cursor()
                    sql="SELECT Session.ClientID, Clients.Forename, Clients.Surname FROM Session INNER JOIN Clients ON Session.ClientID=Clients.ClientID WHERE SeshID=?"
                    cursor.execute(sql,(str(self.pudata[0][0]),))
                    egrab=cursor.fetchall()
                    en.append(egrab[0])
            en2=str(en[0][0]),en[0][1],en[0][2]
            self.ce.append(en2)
            self.celist.set(self.ce)
    
    def Editlistbox(self,click):
        Search=self.search.get()
        Date=self.cal.get_date()
        if Search=="All":
            sql="SELECT ClassID,Trainer_ID,Time From Class WHERE Date=?"
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                cursor.execute(sql,(Date,))
                self.dbtdt=cursor.fetchall()
                sql2="SELECT SeshID,Trainer_ID,Time From Session WHERE Date=?"
                cursor.execute(sql2,(Date,))
                self.dbtdt.extend(cursor.fetchall())
        elif Search=="Class":
            sql="SELECT ClassID,Trainer_ID,Time From Class WHERE Date=?"
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                cursor.execute(sql,(Date,))
                self.dbtdt=cursor.fetchall()
        elif Search=="1:1":
            sql="SELECT SeshID,Trainer_ID,Time From Session WHERE Date=?"
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                cursor.execute(sql,(Date,))
                self.dbtdt=cursor.fetchall()
        elif Search==self.Trainer_ID+" All":
            sql="SELECT ClassID,Trainer_ID,Time From Class WHERE Date=? AND Trainer_ID=?"
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                cursor.execute(sql,(Date,self.Trainer_ID))
                self.dbtdt=cursor.fetchall()
                sql2="SELECT SeshID,Trainer_ID,Time From Session WHERE Date=? AND Trainer_ID=?"
                cursor.execute(sql2,(Date,self.Trainer_ID))
                self.dbtdt.extend(cursor.fetchall())
        elif Search==self.Trainer_ID+" Class":
            sql="SELECT ClassID,Trainer_ID,Time From Class WHERE Date=? AND Trainer_ID=?"
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                cursor.execute(sql,(Date,self.Trainer_ID))
                self.dbtdt=cursor.fetchall()
        elif Search==self.Trainer_ID+" 1:1":
            sql="SELECT SeshID,Trainer_ID,Time From Session WHERE Date=? AND Trainer_ID=?"
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                cursor.execute(sql,(Date,self.Trainer_ID))
                self.dbtdt=cursor.fetchall()
        self.tdt.set(self.dbtdt)
    
    def Pullque(self):
        quet=Toplevel()
        quet.geometry('400x125')
        if int(self.pudata[0][0])>=5000 and int(self.pudata[0][0])<=5999:
            clique=Queue()
            name=str(self.pudata[0][0])+str(self.pudata[0][1])
            Queue.Retrieve(clique,name)
            Label(quet,text="Client Queue "+str(clique.queue)).place(x=25,y=12)
            Label(quet,text="head:"+str(clique.head)).place(x=25,y=35)
            Label(quet,text="tail:"+str(clique.tail)).place(x=75,y=35)
            Label(quet,text="size:"+str(clique.size)+"/"+str(clique.msize)).place(x=125,y=35)
        Button(quet,text="Exit",command=lambda Tk=quet:[Tk.destroy()]).place(x=350,y=35)  

class EquipmentPage():
    def __init__(self,master,Trainer_ID):
        self.master=master
        self.Trainer_ID=Trainer_ID
        self.master.title("Equipment Page")
        self.master.geometry('625x200')
        cqueue=Button(self.master,text="Check Queue",command=self.Cqueue).place(x=425,y=25)
        self.hold=Frame(self.master,height=150,width=300,background='red')
        self.hold.place(x=15,y=25)
        requeststock=Button(self.master,text="Request Stock",command=self.requests).place(x=525,y=25)
        exit=Button(self.master,text="Exit",command=lambda Tk=self.master:[Tk.destroy()]).place(x=15,y=165)
        requestnewequk=Button(self.master,text="Request New Equipment",command=self.requestnew).place(x=450,y=165)
        self.Equtable()
    
    def requests(self):
        idee=self.id[0][1]
        current=self.id[0][2]
        max=self.id[0][3]
        req=Toplevel(self.master)
        myGui=Requests(req,idee,current,max)

    def requestnew(self):
        idee=""
        current=0
        max=0
        req=Toplevel(self.master)
        myGui=Requests(req,idee,current,max)
        
    def Cqueue(self):
        try:
            eque=Queue()
            name=str(self.id[0][0])
            Queue.Retrieve(eque,name)
            quet=Toplevel()
            quet.geometry('400x125')
            Label(quet,text="Client Queue "+str(eque.queue)).place(x=25,y=12)
            Label(quet,text="head:"+str(eque.head)).place(x=25,y=35)
            Label(quet,text="tail:"+str(eque.tail)).place(x=75,y=35)
            Label(quet,text="size:"+str(eque.size)+"/"+str(eque.msize)).place(x=125,y=35)
            Button(quet,text="Exit",command=lambda Tk=quet:[Tk.destroy()]).place(x=350,y=35)  
        except:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Queue empty', 'Equipment Queue', )
    
    def Equtable(self):
        self.id=[]
        try:
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                esql="SELECT * FROM Equipment WHERE EquipmentID!=2000"
                cursor.execute(esql,())
                equipid=cursor.fetchall()
        except:
            equipid=["","","",""]
        self.tree= ttk.Treeview(self.hold,column=(self.hold,"column1", "column2", "column3", "column4"), show='headings',height=5)
        self.tree.heading("#1", text="Equipment")
        self.tree.column("#1", width=100)
        self.tree.heading("#2", text="Name")
        self.tree.column("#2", width=100)
        self.tree.heading("#3", text="Reserved")
        self.tree.column("#3", width=100)
        self.tree.heading("#4", text="Stock")
        self.tree.column("#4", width=100)
        self.tree.column("#5", width=0)
        self.tree.pack(side=LEFT)
        for row in equipid:
            self.tree.insert("", tkinter.END, values=row)
        self.tree.bind("<Double-1>",lambda id=self.id,tree=self.tree:[self.id.insert(0,self.tree.item(self.tree.focus(),'values'))])

class Queue():
    def __init__(self):
        self.queue=[]
        self.head=0
        self.tail=0
        self.msize=10
        self.size=0
    def Enqueue(self,x):
        if self.size==self.msize:
            print("Queue Full (Overflow Error")
        elif self.size<self.msize:
            self.queue.append(self.tail)
            self.tail=self.tail+1
            if self.tail==self.msize:
                self.tail=0
            Queue.Size(self)
    def Dequeue(self):
        if self.size==0:
            print("Queue is empty (Underflow error)")
        elif self.size>0:
            self.head=self.head+1
            Queue.Size(self)
    def Size(self):
        if self.tail>=self.head and self.head==0:
            self.size=self.tail-1
        elif self.tail>=self.head and self.head>0:
            self.size=self.tail-self.head
            print("size",self.size)
        elif self.head>self.tail:
            self.size=self.msize-(self.head-self.tail)
    def Save(self,name):
        fqueue=[]
        fqueue.extend(self.queue[self.head:self.tail+1])
        df = pd.DataFrame(fqueue)
        writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='welcome', index=False)
        writer.save()
    
    def Retrieve(self,name):
        hold= pd.read_excel(name+'.xlsx')
        try:
            self.queue=list(hold[0])
        except:
            self.queue=[]
        self.head=0
        self.tail=len(self.queue)+1
        self.size=len(self.queue)

class PQueue(Queue):
    def __init__(self,Queue):
        super().__init__()
        name="requests"
        try:
            hold= pd.read_excel(name+'.xlsx',header=0)
            count=hold[0].count()
            for x in range(count):
                holder=list(pd.read_excel(name+'.xlsx',header=x+1))
                lists=[holder[0],holder[1],holder[2],holder[3]]
                self.queue.append(lists)
            self.head=0
            self.tail=len(self.queue)+1
            print("tail",self.tail)
            self.size=len(self.queue)
        except:
            pass
    def PEnqueue(self,item,priority):
        if self.size==self.msize:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Queue Overflow Error', 'Requests', )
        else:
            self.queue.insert(priority,item)
            self.tail=self.tail+1
            PQueue.Size(self)
            name="requests"
            PQueue.Save(self,name)
    def PDequeue(self):
        if self.size==0:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Queue Underflow Error', 'Requests', )
        else:
            PQueue.Dequeue(self)
            name="requests"
            PQueue.Save(self,name)

class LinearSearch():
    def search(item,list,listsize):
        print("listsize",listsize)
        z=0
        for x in range (int(listsize)):
            if str(list[x][1])==str(item):
                z=z+1
        return z

class ManagerPage():
    def __init__(self,master,Trainer_ID):
        self.master=master
        self.Trainer_ID=Trainer_ID
        self.master.title("Manager Page")
        self.master.geometry('300x300')
        Button(self.master,text="Reset Trainers",command=self.Rtra).place(x=25,y=25)
        Button(self.master,text="Reset Clients",command=self.Rcli).place(x=190,y=25)
        Button(self.master,text="Reset Sessions",command=self.Rses).place(x=25,y=75)
        Button(self.master,text="Reset Equipment",command=self.Requ).place(x=190,y=75)
        Button(self.master,text="Reset all",command=self.R).place(x=120,y=125)
        Button(self.master,text="View Request",command=self.Req).place(x=25,y=175)
        Button(self.master,text="View Log",command=self.Log).place(x=190,y=175)
        Button(self.master,text="Delete Trainers",command=self.Deltrainer).place(x=120,y=225)     
   
    def Rtra(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            mansql="SELECT * FROM Trainers WHERE Trainer_ID=3000"
            cursor.execute(mansql)
            manager=cursor.fetchall()
            dsql="DROP TABLE Trainers"
            cursor.execute(dsql)
            csql='CREATE TABLE "Trainers" ("Trainer_ID"	INTEGER,"Forename"	TEXT,"Surname"	TEXT,"Password"	TEXT,"Phone"	TEXT,"BEmail"	TEXT,"DOB"	TEXT,"Address"	TEXT,"Sex"	TEXT,PRIMARY KEY("Trainer_ID"))'
            cursor.execute(csql) 
            asql="INSERT INTO Trainers(Trainer_ID,Forename,Surname,Password,Phone,BEmail,DOB,Address,Sex) VALUES(?,?,?,?,?,?,?,?,?)"
            cursor.execute(asql,(manager[0][0],manager[0][1],manager[0][2],manager[0][3],manager[0][4],manager[0][5],manager[0][6],manager[0][7],manager[0][8]))
   
    def Rcli(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            dsql="DROP TABLE Clients"
            cursor.execute(dsql)
            d2sql="DROP TABLE Info"
            cursor.execute(d2sql)
            csql="""CREATE TABLE "Clients" (
                        "ClientID"	INTEGER,
                        "Trainer_ID"	INTEGER,
                        "Forename"	TEXT,
                        "Surname"	TEXT,
                        "Password"	TEXT,
                        "Phone"	TEXT,
                        "Email"	TEXT,
                        "DOB"	TEXT,
                        "Address"	TEXT,
                        PRIMARY KEY("ClientID")
                    );"""
            cursor.execute(csql)
            c2sql="""CREATE TABLE "Info" (
                        "Info_ID"	INTEGER,
                        "ClientID"	INTEGER,
                        "Height"	TEXT,
                        "Weight"	TEXT,
                        "Calorie"	TEXT,
                        "Sex"	TEXT,
                        PRIMARY KEY("Info_ID")
                    );"""
            cursor.execute(c2sql)
   
    def Rses(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            ssql="SELECT ClassID,EReservationID,CReservationID From Class"
            cursor.execute(ssql)
            sce=cursor.fetchall()
            try:
                for x in range(len(sce)):
                    name=str(sce[x][0])+str(self.Trainer_ID)
                    os.remove(name+".xlsx")
                    gre="SELECT EquipmentID FROM SeshEqu WHERE EReservationID=?"
                    cursor.execute(gre,(sce[x][1],))
                    equipid=cursor.fetchall()
                    upe="UPDATE Equipment SET Reserved=Reserved-1 WHERE EquipmentID=?"
                    cursor.execute(upe,(equipid[0][0],))
                    try:
                        sql3="SELECT EquipmentID FROM Equipment"
                        cursor.execute(sql3,())
                        id=cursor.fetchall()
                        for x in range(len(id)):
                            que=Queue()
                            name=str(id[x][0])
                            try:
                                Queue.Retrieve(que,name)
                                que.queue.remove(sce[x][0])
                            except:
                                pass
                        Queue.Save(que,name)
                    except:
                        pass
            except:
                pass
            for x in range(len(sce)):
                name=str(sce[x][2])
                os.remove(name+".xlsx")
                ssql="SELECT EReservationID From Session"
            cursor.execute(ssql)
            sce=cursor.fetchall()
            try:
                for x in range(len(sce)):
                    gre="SELECT EquipmentID FROM SeshEqu WHERE EReservationID=?"
                    cursor.execute(gre,(sce[x][1],))
                    equipid=cursor.fetchall()
                    upe="UPDATE Equipment SET Reserved=Reserved-1 WHERE EquipmentID=?"
                    cursor.execute(upe,(equipid[0][0],))
                    try:
                        sql3="SELECT EquipmentID FROM Equipment"
                        cursor.execute(sql3,())
                        id=cursor.fetchall()
                        for x in range(len(id)):
                            que=Queue()
                            name=str(id[x][0])
                            try:
                                Queue.Retrieve(que,name)
                                que.queue.remove(sce[x][0])
                            except:
                                pass
                        Queue.Save(que,name)
                    except:
                        pass
            except:
                pass
            dsql="DROP TABLE Session"  
            d2sql="DROP TABLE Class"  
            cursor.execute(dsql)
            cursor.execute(d2sql)
            c1sql="""CREATE TABLE "Session" (
                        "SeshID"	INTEGER,
                        "Trainer_ID"	INTEGER,
                        "ClientID"	INTEGER,
                        "EReservationID"	TEXT,
                        "Date"	TEXT,
                        "Time"	TEXT,
                        "Duration"	TEXT,
                        "Studio"	TEXT,
                        PRIMARY KEY("SeshID")
                    );"""
            cursor.execute(c1sql)
            c2sql="""CREATE TABLE "Class" (
                        "ClassID"	INTEGER,
                        "Trainer_ID"	INTEGER,
                        "CReservationID"	TEXT,
                        "EReservationID"	TEXT,
                        "Date"	TEXT,
                        "Time"	TEXT,
                        "Duration"	TEXT,
                        "Studio"	TEXT,
                        "Current"	TEXT,
                        "Max"	TEXT,
                        PRIMARY KEY("ClassID")
                    );"""
            cursor.execute(c2sql)             
   
    def Requ(self):
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            ssql="SELECT EquipmentID From Equipment WHERE EquipmentID!=2000"
            sql="SELECT EquipmentID,Name FROM Equipment WHERE EquipmentID=2000"
            cursor.execute(ssql)
            e=cursor.fetchall()
            for x in range(len(e)):
                name=str(e[x][0])
                os.remove(name+".xlsx")
            dsql="DROP TABLE Equipment"   
            cursor.execute(dsql)
            c1sql="""CREATE TABLE "Equipment" (
                        "EquipmentID"	INTEGER,
                        "Name"	TEXT,
                        "Reserved"	INTEGER,
                        "Stock"	INTEGER,
                        PRIMARY KEY("EquipmentID")
                    );"""
            cursor.execute(c1sql)
            asql="INSERT INTO Equipment(EquipmentID,Name,Reserved,Stock) VALUES(?,?,?,?)"
            cursor.execute(asql,(2000,"No Equipment",0,99))
   
    def R(self):
        self.Rtra()
        self.Rcli()
        self.Rses()
        self.Requ()
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            dsql="DROP TABLE Log"   
            cursor.execute(dsql)
            c1sql="""CREATE TABLE "Log" (
                        "Record"	INTEGER,
                        "Trainer_ID"	INTEGER,
                        "Date"	TEXT,
                        "Time"	TEXT,
                        "Reason"	TEXT,
                        PRIMARY KEY("Record")
                    );"""
            cursor.execute(c1sql)
   
    def Req(self):
        reqroot=Toplevel()
        self.master=reqroot
        self.master.title('Requests')
        self.master.geometry('350x250')
        self.request=PQueue(Queue)
        try:
            self.currentqueue=self.request.queue[self.request.head]
            self.cal=RPNStack()
            o="*"
            ans=self.cal.Start(self.currentqueue[3],self.currentqueue[2],o)
            reason="More Stock"
            z=LinearSearch.search(reason,self.request.queue,self.request.size)
            print("z",z)
            t=self.request.size-int(z)
            print("t",t)
            if t<=0:
                t=0
            self.el=Label(self.master,text="Equipment:"+str(self.currentqueue[0]),)
            self.el.place(x=25,y=25)
            self.rl=Label(reqroot,text="Reason:"+str(self.currentqueue[1]),)
            self.rl.place(x=25,y=50)
            self.pl=Label(self.master,text="Price £"+str(self.currentqueue[2]),)
            self.pl.place(x=25,y=75)
            self.tl=Label(self.master,text="Total £"+str(ans),)
            self.tl.place(x=160,y=75)
            self.nsl=Label(self.master,text=str(z)+" requests for more stock.",)
            self.nsl.place(x=160,y=25)
            self.nel=Label(self.master,text=str(t)+" requests for new equipment.",)
            self.nel.place(x=160,y=50)
            self.ql=Label(self.master,text="Quantity:"+str(self.currentqueue[3]),)
            self.ql.place(x=25,y=100)
            Button(self.master,text="Deny",command=self.Decline).place(x=25,y=150)
            Button(self.master,text="Accept",command=self.Accept).place(x=190,y=150)
            Button(self.master,text="Exit",command=lambda Tk=self.master:[Tk.destroy()]).place(x=125,y=170)
        except:
            self.Decline()
   
    def Decline(self):
        print("decline")
        self.request.PDequeue()
        self.request.Size()
        self.request=PQueue(Queue)
        try:
            o="*"
            self.currentqueue=self.request.queue[self.request.head]
            ans=self.cal.Start(self.currentqueue[3],self.currentqueue[2],o)
            reason="More Stock"
            z=LinearSearch.search(reason,self.request.queue,self.request.size)
            print("z",z)
            t=self.request.size-int(z)
            print("t",t)
            if t<=0:
                t=0
            self.el.configure(text="Equipment:"+str(self.currentqueue[0]),)
            self.rl.configure(text="Reason:"+str(self.currentqueue[1]),)
            self.pl.configure(text="Price:"+str(self.currentqueue[2]),)
            self.ql.configure(text="Quantity:"+str(self.currentqueue[3]),)
            self.tl.configure(text="Total £"+str(ans),)
            self.nel.configure(text=str(t)+" requests for new equipment.",)
            self.nsl.configure(text=str(z)+" requests for more stock.",)
        except:
            self.master.destroy()
   
    def Accept(self):
        print("accept")
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            sql="SELECT COUNT(EquipmentID) From Equipment"
            cursor.execute(sql,)
            count=cursor.fetchall()
            sql="SELECT EquipmentID,Name From Equipment"
            cursor.execute(sql,)
            name=cursor.fetchall()
            if self.currentqueue[1]=="More Stock":
                for x in range(int(count[0][0])):
                    if self.currentqueue[0]==name[x][1]:
                        sql="UPDATE Equipment SET Stock=Stock+? WHERE EquipmentID=?"
                        cursor.execute(sql,(int(self.currentqueue[3]),int(name[x][0]),))
            elif self.currentqueue[1]!="More Stock":
                sql="SELECT MAX(EquipmentID) From Equipment"
                cursor.execute(sql,)
                maxid=cursor.fetchall()
                maxid=int(maxid[0][0])+1
                addsql="INSERT INTO Equipment(EquipmentID,Name,Reserved,Stock) VALUES(?,?,?,?)"
                cursor.execute(addsql,(maxid,self.currentqueue[0],str(0),str(self.currentqueue[3])))  
                df = pd.DataFrame()
                writer = pd.ExcelWriter(str(maxid)+'.xlsx', engine='xlsxwriter')
                df.to_excel(writer, sheet_name='welcome', index=False)
                writer.save()
        self.request.PDequeue()
        self.request.Size()
        self.request=PQueue(Queue)
        try:
            o="*"
            self.currentqueue=self.request.queue[self.request.head]
            ans=self.cal.Start(self.currentqueue[3],self.currentqueue[2],o)
            reason="More Stock"
            z=LinearSearch.search(reason,self.request.queue,self.request.size)
            t=self.request.size-int(z)
            print("z",z)
            print("t",t)
            if t<=0:
                t=0
            self.el.configure(text="Equipment:"+str(self.currentqueue[0]),)
            self.rl.configure(text="Reason:"+str(self.currentqueue[1]),)
            self.pl.configure(text="Price:"+str(self.currentqueue[2]),)
            self.ql.configure(text="Quantity:"+str(self.currentqueue[3]),)
            self.tl.configure(text="Total £"+str(ans),)
            self.nel.configure(text=str(t)+" requests for new equipment.",)
            self.nsl.configure(text=str(z)+" requests for more stock.",)
        except:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Queue Underflow Error', 'Requests', )
            self.master.destroy()
   
    def Log (self):
        logroot=Toplevel()
        self.master=logroot
        self.master.title('Log')
        self.master.geometry('500x450')
        self.dd=StringVar()
        self.cal = Calendar(self.master,font="Arial 14", selectmode='day',date_pattern='mm/dd/yy',cursor="hand1",background='Black',foreground='Orange')
        self.cal.pack(fill="x")
        self.fsearch=Listbox(self.master,selectmode=BROWSE,listvariable=self.dd,)
        self.fsearch.pack(fill="both")
        Button(self.master,text="Exit",command=lambda Tk=self.master:[Tk.destroy()]).pack(fill="both")
        self.cal.bind('<<CalendarSelected>>',self.logbox)  
   
    def logbox(self,event):
        Date=self.cal.get_date()
        sql="SELECT * From Log WHERE Date=?"
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            cursor.execute(sql,(Date,))
            self.d=cursor.fetchall()
        self.dd.set(self.d)
   
    def Deltrainer(self):
        traroot=Toplevel()
        self.master=traroot
        self.master.geometry('400x150')
        self.master.title('Trainers')
        self.choosen=StringVar()
        with sqlite3.connect("DATABASEV1.db") as connection:
            cursor=connection.cursor()
            sql="SELECT * FROM Trainers WHERE Trainer_ID!=?"
            cursor.execute(sql,(self.Trainer_ID,))
            trainers=cursor.fetchall()
            self.trainerlist=[]
            for x in range(len(trainers)):
                self.trainerlist.append(trainers[x][0:3])
            self.trainerchoose=ttk.Combobox(self.master,textvariable=self.choosen,values=self.trainerlist,width=50)
            self.trainerchoose.pack()
        self.trainerchoose.bind('<<ComboboxSelected>>',self.delete)
        self.trainerchoose.bind('<<KeyRelease >>',self.Gthread)
   
    def Gthread(self,event):
        gthread=Thread(target=self.GoogleRipOff)
        gthread.start()
   
    def GoogleRipOff(self):
        cholen=int(len(self.choosen.get()))
        chosen=self.choosen.get()
        if cholen!=0:
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT Trainer_ID, Forename, Surname FROM Trainers WHERE Trainer_ID!=? AND SUBSTR(Forename, 1, ?) = ?  OR SUBSTR(Surname, 1, ?) = ? ORDER BY Trainer_ID"
                cursor.execute(sql,(self.Trainer_ID,cholen,chosen,cholen,chosen,))
                new=cursor.fetchall()
                self.trainerlist.clear()
                self.trainerlist=new
        elif cholen==0:
            with sqlite3.connect("DATABASEV1.db") as connection:
                cursor=connection.cursor()
                sql="SELECT * FROM Trainers WHERE Trainer_ID!=?"
                cursor.execute(sql,(self.Trainer_ID,))
                trainers=cursor.fetchall()
                self.trainerlist=[]
            for x in range(len(trainers)):
                self.trainerlist.append(trainers[x][0:3])
            self.trainerchoose.config(values=self.trainerlist)
    
    def delete(self,event):
        choosen=self.choosen.get()
        Trainer_ID=choosen[0:5]
        with sqlite3.connect("DATABASEV1.db") as db:
            cursor=db.cursor()
            sql="DELETE FROM Trainers WHERE Trainer_ID=?"
            cursor.execute(sql,(Trainer_ID,))
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Trainer Deleted', 'Trainers', )
                     
class RPNStack():
    def Start(self,q,p,o):
        self.rpnstack=[]
        self.calculate=0
        self.operators=['*']
        self.pointer=-1
        self.equa=[q,p,o]
        self.size=0
        for x in range(3):
            if str(self.equa[0])==str(self.operators[0]):
                return int(self.rpnstack[self.pointer])*int(self.rpnstack[self.pointer-1])
            elif str(self.equa[0])!=self.operators[0]:
                RPNStack.Append(self)
    def Append(self):
        self.pointer=self.pointer+1
        self.rpnstack.append(self.equa[0])
        self.equa.pop(0)
        self.size+1
    
      
        
        
    
    def Pop(self):
        pass

class Requests():
    def __init__(self,master,idee,current,max):
        self.master=master
        self.master.title('Requests')
        self.master.geometry('250x250')
        self.idee=idee
        self.current=current
        self.max=max
        self.quantl=[1,2,3,4,5]
        self.reason=StringVar()
        self.name=StringVar()
        self.quant=StringVar()
        self.price=StringVar()
        Label(self.master,text="Name Of Equipment:").place(x=20,y=20)
        self.equnam=Entry(self.master,textvariable=self.name)
        self.equnam.place(x=20,y=40)
        Label(self.master,text="Reason:").place(x=20,y=60)
        self.rea=Entry(self.master,textvariable=self.reason)
        self.rea.place(x=20,y=80)
        Label(self.master,text="Quantity").place(x=160,y=20)
        quant=OptionMenu(self.master,self.quant,*self.quantl).place(x=160,y=40)
        Label(self.master,text="£").place(x=200,y=80)
        price=Entry(self.master,textvariable=self.price,width=5).place(x=160,y=80)
        Button(self.master,text="Send Request",command=self.SendReq,width=25).place(x=20,y=140)
        if self.idee!="":
            self.equnam.configure(state='disabled')
            self.name.set(self.idee)
            self.rea.configure(state='disable')
            self.reason.set('More Stock')
    
    def SendReq(self):
        req=PQueue(Queue)
        Name=self.equnam.get()
        Reason=self.reason.get()
        try:
            Price=round(float(self.price.get()))
        except:
            Price=self.price.get()
        Quantity=self.quant.get()
        item=[Name,Reason,Price,Quantity]
        if int(self.current)==0 and int(self.max)==0:
            priority=0
        elif int(self.current)<int(self.max)//2:
            priority=3
        elif int(self.current)==int(self.max)//2:
            priority=2
        elif int(self.current)>int(self.max)//2:
            priority=1
        PQueue.PEnqueue(req,item,priority)
        self.master.destroy()

def main():
    root=Tk()
    myGUIWelcome=Mainwindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
