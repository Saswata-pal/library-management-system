from tkinter import *
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage, Label, Frame
from tkcalendar import *
import sqlite3
import time
import datetime
from datetime import datetime
from datetime import timedelta
from PIL import Image, ImageTk
import smtplib
import os
import sys

db = sqlite3.connect('admin.db')
dd=sqlite3.connect('storebook.db')
dc=sqlite3.connect('students.db')

root = Tk()
root.title("Library Management System")
root.iconbitmap("lib.ico")
root.geometry("900x500+200+100")
root.resizable(0, 0)

class maincode:
     def login(self):

         self.var1 = self.e1.get()
         self.var2 = self.e2.get()
         cursor=db.cursor()
         cursor.execute("SELECT * FROM adm WHERE User_ID='"+self.var1+"' and Password='"+self.var2+"'")
         db.commit()
         self.ab = cursor.fetchone()
         if self.ab!=None:
               #messagebox.showinfo('Library System',ab[1])
             self.under_fm=Frame(root,height=500,width=900,bg='#fff')
             self.under_fm.place(x=0,y=0)
             self.fm2=Frame(root,bg='#4682b4',height=80,width=900)
             self.fm2.place(x=0,y=0)

             lgo=Canvas(self.fm2,bg='#4682b4',height=200,width=100,bd=4,relief='flat')
             lgo.place(x=0,y=0)

             self.lbb=Label(self.fm2,bg='#4682b4')
             self.lbb.place(x=15,y=5)
             self.ig= PhotoImage(file= ('library.png'))
             self.lbb.config(image=self.ig)
             self.lb3=Label(self.fm2,text='Library System',fg='Yellow',bg='#4682b4',font=('Garamond',30,'bold'))
             self.lb3.place(x=325,y=17)


             #----------------------------name------------------------

             self.name=Label(root,text="Name : ",bg='#fff',fg="black",font=('Arial',10,'bold'))
             self.name.place(x=5,y=83)
             self.name1=Label(root,text=self.ab[1],fg='black',bg='#fff',font=('Arial',10,'bold'))
             self.name1.place(x=60,y=83)

             #------------------------date-------------------------

             self.today=date.today()
             self.dat=Label(root,text='Date : ',bg='#fff',fg='black',font=('Arial', 10, 'bold'))
             self.dat.place(x=740,y=83)
             self.dat2 = Label(root, text=self.today, bg='#fff', fg='black', font=('Arial', 10, 'bold'))
             self.dat2.place(x=790, y=83)

             self.cur()

         else:
               messagebox.showerror('Library System', 'Your ID or Password is not Valid')
             #---------------------------------------------------------

     def add_student(self,event=None):
        add_student_window = Toplevel(root)
        add_student_window.title("Add Student")
        add_student_window.geometry("400x500+590+208")
        add_student_window.iconbitmap( ("lib.ico"))
        add_student_window.resizable(0, 0)
        add_student_window.configure(bg="#090c36")

          # Heading label
        heading = Label(add_student_window, text="Add New Student", 
        font=('Palatino', 18, 'bold'), bg="#090c36", fg="#d4f037")
        heading.place(x=100, y=20)

        label1 = Label(add_student_window, text="Name:", bg="#090c36", fg="#d4f037", font=('Verdana', 10, 'bold'))
        label1.place(x=40, y=80)
        name_entry = Entry(add_student_window, width=30, font=('Verdana', 10))
        name_entry.place(x=120, y=80)

        label2 = Label(add_student_window, text="ERP ID:", bg="#090c36", fg="#d4f037", font=('Verdana', 10, 'bold'))
        label2.place(x=40, y=130)
        erp_id_entry = Entry(add_student_window, width=30, font=('Verdana', 10))
        erp_id_entry.place(x=120, y=130)

        label3 = Label(add_student_window, text="Course:", bg="#090c36", fg="#d4f037", font=('Verdana', 10, 'bold'))
        label3.place(x=40, y=180)
        course_entry = Entry(add_student_window, width=30, font=('Verdana', 10))
        course_entry.place(x=120, y=180)


        label4 = Label(add_student_window, text="Year:", bg="#090c36", fg="#d4f037", font=('Verdana', 10, 'bold'))
        label4.place(x=40, y=230)
        year_entry = Entry(add_student_window, width=30, font=('Verdana', 10))
        year_entry.place(x=120, y=230)

        label5 = Label(add_student_window, text="Roll No:", bg="#090c36", fg="#d4f037", font=('Verdana', 10, 'bold'))
        label5.place(x=40, y=280)
        roll_no_entry = Entry(add_student_window, width=30, font=('Verdana', 10))
        roll_no_entry.place(x=120, y=280)

        label6 = Label(add_student_window, text="Email:", bg="#090c36", fg="#d4f037", font=('Verdana', 10, 'bold'))
        label6.place(x=40, y=330)
        email_entry = Entry(add_student_window, width=30, font=('Verdana', 10))
        email_entry.place(x=120, y=330)
       
        label7 = Label(add_student_window, text="Mobile No:", bg="#090c36", fg="#d4f037", font=('Verdana', 9, 'bold'))
        label7.place(x=40, y=380)
        contact_no_entry = Entry(add_student_window, width=30, font=('Verdana', 10))
        contact_no_entry.place(x=120, y=380)

        def submit():
            try:
                 conn = sqlite3.connect('students.db')
                 cursor = conn.cursor()

                 erp_id = erp_id_entry.get()
                 Name = name_entry.get()
                 course = course_entry.get()
                 year = year_entry.get()
                 roll_no = roll_no_entry.get()
                 email = email_entry.get()
                 contact_no = contact_no_entry.get()

                 #check for empty entries
                 if not all([erp_id, Name, course, year, roll_no, email, contact_no]):
                      messagebox.showerror("Error", "All fields are required. Please fill in all fields.")
                      return

                 # Check if ERP ID, Contact No. and Roll No. already exists
                 cursor.execute("SELECT * FROM student WHERE ERP_ID = ?", (erp_id,))
                 if cursor.fetchone():
                    messagebox.showerror("Error", "This ERP ID already exists. Please use a different ID.")
                    add_student_window.destroy()
                    return

                 cursor.execute("SELECT * FROM student WHERE Roll_No = ?", (roll_no,))
                 if cursor.fetchone():
                    messagebox.showerror("Error", "This roll number already exists. Please use a different roll number.")
                    add_student_window.destroy()
                    return

                 cursor.execute("SELECT * FROM student WHERE Contact_no = ?", (contact_no,))
                 if cursor.fetchone():
                    messagebox.showerror("Error", "This contact number already exists. Please use a different number.")
                    add_student_window.destroy()
                    return

                 cursor.execute("INSERT INTO student (ERP_ID, Name, Course, year, Roll_No, \"e-mail\", Contact_no, College) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (erp_id, Name, course, year, roll_no, email, contact_no, 'The neotia university'))

                 conn.commit()
                 messagebox.showinfo("Success", "Student added successfully!")
                 add_student_window.destroy()
            except Exception as e:
                 messagebox.showerror("Error", f"An error occurred: {str(e)}")
                 print(e)
            finally:
                 conn.close()
                 

        submit_button = Button(add_student_window, text="Submit", command=submit, bg="#28a745", fg="#d4f037", font=('arial', 9, 'bold'))
        submit_button.place(x=160, y=430)

     button3 = Button(root, text="Add Student", command=add_student, bg="#28a745", fg="#3be3db", font=('arial', 10, 'bold'))
     button3.place(x=300, y=190)

     def cur(self):
             self.fm3=Frame(root,bg='#fff',width=900,height=390)
             self.fm3.place(x=0,y=110)

             image_path = "bg66.png"
             bg_image = Image.open(image_path)
             bg_image = bg_image.resize((900, 390), Image.LANCZOS)  
             background_image = ImageTk.PhotoImage(bg_image)
             
             # resized background image
             background_label = Label(self.fm3, image=background_image)
             background_label.image = background_image  # keeping reference 2 avoid garbage collection
             background_label.place(x=0, y=0, relwidth=1, relheight=1) 



             #------------------------Clock---------------------------

             def clock():
                 h = str(time.strftime("%H"))
                 m = str(time.strftime("%M"))
                 s = str(time.strftime("%S"))

                 if int(h) >=12 and int(m) >=0:
                       self.lb7_hr.config(text="PM")

                 if int(h) > 12:
                     h = str(int(h) - 12)

                 self.lb1_hr.config(text=h)
                 self.lb3_hr.config(text=m)
                 self.lb5_hr.config(text=s)

                 self.lb1_hr.after(200, clock)

             self.lb1_hr = Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#fc1c1c', fg='white')
             self.lb1_hr.place(x=560, y=0, width=60, height=30)


             self.lb3_hr = Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#0ee38b', fg='white')
             self.lb3_hr.place(x=630, y=0, width=60, height=30)


             self.lb5_hr = Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#2b1dff', fg='white')
             self.lb5_hr.place(x=700, y=0, width=60, height=30)


             self.lb7_hr = Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#2b1dff', fg='white')
             self.lb7_hr.place(x=770, y=0, width=60, height=30)


             clock()

             #-------------------------------clock closed------------------------

             # developer name--------------------
             
             self.develop=Label(self.fm3,text='Developed By - Saswata',bg='#fff',fg='blue',
                               font=('Cursive',12,'italic','bold'))
             self.develop.place(x=600,y=350)

             #-----------------addbutton-----------------

             self.bt1=Button(self.fm3,text='  Add Books',fg='#07023d',bg='#f6fa07',font=('Fixedsys',15,'bold'),width=170,
                          height=0,bd=7,relief='flat',command=self.addbook,cursor='hand2')
             self.bt1.place(x=40,y=40)
             self.logo = PhotoImage(file='bt1.png')
             self.bt1.config(image=self.logo, compound=LEFT)
             self.small_logo = self.logo.subsample(1,1)
             self.bt1.config(image=self.small_logo)

             #------------------Issuebutton--------------

             self.bt2 = Button(self.fm3, text='  Issue Books', fg='#07023d', bg='#f6fa07', font=('Fixedsys', 15, 'bold'),
                            width=170,height=0, bd=7,relief='flat',command=self.issuebook,cursor='hand2')
             self.bt2.place(x=250, y=40)
             self.log = PhotoImage(file='bt2.png')
             self.bt2.config(image=self.log, compound=LEFT)
             self.small_log = self.log.subsample(1, 1)
             self.bt2.config(image=self.small_log)

             #---------Editbutton----------------

             self.bt3 = Button(self.fm3, text='  Edit Books', fg='#07023d', bg='#f6fa07', font=('Fixedsys', 15, 'bold'),
                           width=170,height=0,bd=7,relief='flat',cursor='hand2',command=self.edit)
             self.bt3.place(x=40, y=120)
             self.logb = PhotoImage(file='bt3.png')
             self.bt3.config(image=self.logb, compound=LEFT)
             self.small_logb = self.logb.subsample(1, 1)
             self.bt3.config(image=self.small_logb)

             #-----------------Returnbutton----------------

             self.bt4 = Button(self.fm3, text='  Return Books', fg='#07023d', bg='#f6fa07', font=('Fixedsys', 15, 'bold'),
                          width=170,height=0,bd=7,relief='flat',cursor='hand2',command=self.return_book)
             self.bt4.place(x=250, y=120)
             self.log4 = PhotoImage(file='bt4.png')
             self.bt4.config(image=self.log4, compound=LEFT)
             self.small_log4 = self.log4.subsample(1, 1)
             self.bt4.config(image=self.small_log4)

             #----------------------Deletebutton---------------------

             self.bt5 = Button(self.fm3, text=' Delete Books', fg='#07023d', bg='#f6fa07', font=('Fixedsys', 15, 'bold'),
                          width=170,height=0,bd=7,relief='flat',cursor='hand2',command=self.delete)
             self.bt5.place(x=40, y=200)
             self.log5 = PhotoImage(file='bt5.png')
             self.bt5.config(image=self.log5, compound=LEFT)
             self.small_log5 = self.log5.subsample(1, 1)
             self.bt5.config(image=self.small_log5)

             #--------------------Show Button-----------------------------

             self.bt6 = Button(self.fm3, text='  Show Books', fg='#07023d', bg='#f6fa07', font=('Fixedsys', 15, 'bold'),
                           width=170,height=0,bd=7, relief='flat',cursor='hand2',command=self.show)
             self.bt6.place(x=250, y=200)
             self.log6 = PhotoImage(file='bt6.png')
             self.bt6.config(image=self.log6, compound=LEFT)
             self.small_log6 = self.log6.subsample(1, 1)
             self.bt6.config(image=self.small_log6)

             #-------------------------Seearch Button------------------

             self.bt7 = Button(self.fm3, text=' Search Books', fg='#07023d', bg='#f6fa07', font=('Fixedsys', 15, 'bold'),
                          width=170,height=0,bd=7, relief='flat',cursor='hand2',command=self.search)
             self.bt7.place(x=40, y=280)
             self.log7 = PhotoImage(file='bt7.png')
             self.bt7.config(image=self.log7, compound=LEFT)
             self.small_log7 = self.log7.subsample(1, 1)
             self.bt7.config(image=self.small_log7)

             #---------------------Exit Button-----------------------
             try:

                self.bt8 = Button(self.fm3, text='  Exit', fg='#07023d', bg='#f6fa07', font=('Fixedsys', 15, 'bold'),
                               width=170,
                          height=0, bd=7, relief='flat',cursor='hand2',command=self.code)
                self.bt8.place(x=250, y=280)
                self.log8 = PhotoImage(file='bt8.png')
                self.bt8.config(image=self.log8, compound=LEFT)
                self.small_log8 = self.log8.subsample(1, 1)
                self.bt8.config(image=self.small_log8)

             except:

               self.bt9 = ttk.Button(self.fm3, text="ram", bg='#11d09a', font=('Arial', 15, 'bold'), width=150,
                                     height=0)
               self.bt9.place(x=40, y=350)
               self.log9 = PhotoImage(file='bt8.png')
               self.bt9.config(image=self.log9, compound=LEFT)
               self.small_log9 = self.log9.subsample(3, 3)
               self.bt9.config(image=self.small_log9)
        

     def mainclear(self):
          if root.winfo_exists():
            if self.e1.winfo_exists():
                 self.e1.delete(0, END)
            if self.e2.winfo_exists():
                 self.e2.delete(0, END)



    #-----------------------button add book----------------------

     def addbook(self):
         class temp(maincode):

             def book(self):

                 #main frame
                 self.fm=Frame(root,bg='#1d1c73',width=900,height=390)
                 self.fm.place(x=0,y=110)

                 #load and resize background image setup
                 original_image = Image.open('bg8.png')
                 resized_image = original_image.resize((900, 390), Image.LANCZOS)
                 self.bg_img = ImageTk.PhotoImage(resized_image)

                 # Display the resized background image on a Label
                 self.bg_label = Label(self.fm, image=self.bg_img)
                 self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

                 #form frame
                 self.fm1=Frame(self.fm,bg='#5c94ed',width=500,height=360,bd=5,relief='flat')
                 self.fm1.place(x=200,y=15)

                 #back button
                 self.backbt = Button(self.fm, width=60, bg='#a7ecd9',activebackground='#a7ecd9', bd=0, relief='flat',
                                                                                                 command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)

                 #---------------------------Label---------------------------------
                 self.f=Frame(self.fm1,bg='#1d1c73',width=490,height=35)
                 self.f.place(x=0,y=0)
                 self.ll=Label(self.f,text='ADD BOOKS',fg='#fff',bg='#1d1c73',font=('Bookman Old Style',12,'bold'))
                 self.ll.place(x=200,y=6)
                 self.lb=Label(self.fm1,text='ID',fg='black',bg='#5c94ed',font=('Arial',10,'bold'))
                 self.lb.place(x=70,y=90)
                 self.lb2 = Label(self.fm1, text='Title', fg='black', bg='#5c94ed', font=('Arial', 10, 'bold'))
                 self.lb2.place(x=70, y=130)
                 self.lb3 = Label(self.fm1, text='Author', fg='black', bg='#5c94ed', font=('Arial', 10, 'bold'))
                 self.lb3.place(x=70, y=170)
                 self.lb4= Label(self.fm1, text='Edition', fg='black', bg='#5c94ed', font=('Arial', 10, 'bold'))
                 self.lb4.place(x=70, y=210)
                 self.lb5 = Label(self.fm1, text='Price', fg='black', bg='#5c94ed', font=('Arial', 10, 'bold'))
                 self.lb5.place(x=70, y=250)

                 #-------------------------------Entry-------------------------------------

                 self.ee1=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee1.place(x=180,y=88)
                 self.ee2=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee2.place(x=180,y=130)
                 self.ee3=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee3.place(x=180,y=170)
                 self.ee4=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee4.place(x=180,y=210)
                 self.ee5=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee5.place(x=180,y=250)

                 self.bt=Button(self.fm1,text='Submit',width=41,bg='red',fg='#fff',font=('Arial',10,'bold'),bd=5,
                          relief='flat',command=self.submit1)
                 self.bt.place(x=70,y=290)

                 #---------------------Back button----------------------------------




             def submit1(self):

                 self.id=self.ee1.get()
                 self.ttl=self.ee2.get()
                 self.aut=self.ee3.get()
                 self.edi=self.ee4.get()
                 self.pri=self.ee5.get()
                 cursor=dd.cursor()
                 cursor.execute("INSERT INTO stbook(Book_ID,Title,Author,Edition,Price,Issue,Copies_Available) values(?,?,?,?,?,?,?)",(self.id,
                                                                                                      self.ttl,self.aut,self.edi,self.pri,'Available',10))
                 dd.commit()
                 messagebox.showinfo('Library System','Book added successfully!')
                 self.clear()

             def clear(self):
                 self.ee1.delete(0,END)
                 self.ee2.delete(0,END)
                 self.ee3.delete(0,END)
                 self.ee4.delete(0,END)
                 self.ee5.delete(0,END)

         obj=temp()
         obj.book()


        #-----------xxxxxxxxxxxx--------close add book---xxxxxxxxxxxxxxxxxxxx---------------

        #--------------------------------Issue Books---------------------------------
     def issuebook(self):
         class test(maincode):
              max=0
              n = 1
              def issue(self):
                  self.f = Frame(root, bg='#a7ecd9', width=900, height=390)
                  self.f.place(x=0, y=110)

                  self.fmi=Canvas(self.f,bg='#fff',width=900,height=390,bd=0,relief='flat')
                  self.fmi.place(x=0,y=0)

                  self.fc=Frame(self.fmi,bg='#fff',width=330,height=230,bd=4,relief='flat')
                  self.fc.place(x=70,y=20)

                  self.ffb=Frame(self.fc,bg='#0f624c',bd=2,relief='flat',width=330,height=35)
                  self.ffb.place(x=0,y=0)

                  self.lc=Label(self.ffb,text='STUDENT  INFORMATION',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
                  self.lc.place(x=55,y=5)

                  self.lb=Label(self.fc,text='Roll-No',bg='#fff',fg='black',font=('Arial',10,'bold'))
                  self.lb.place(x=15,y=60)
                  self.ob=Label(self.fc,text='or',bg='#fff',fg='black',font=('cursive',12,'bold'))
                  self.ob.place(x=180,y=90)
                  self.em = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                  self.em.place(x=105, y=60)
                  self.lb = Label(self.fc, text='ERP-ID', bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                  self.lb.place(x=15, y=120)
                  self.em2 = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                  self.em2.place(x=105, y=120)
                  self.bt = Button(self.fc, text='Submit', width=14, bg='red', fg='#fff', font=('Arial', 10, 'bold'),
                                 bd=5,relief='flat',command=self.check)
                  self.bt.place(x=15,y=180)

                  self.bt3=Button(self.fc,text='Clear',width=14,bg='blue',fg='#fff',font=('arial',10,'bold'),bd=5,
                            relief='flat',command=self.clr)
                  self.bt3.place(x=165,y=180)

                  self.backbt = Button(self.fmi,width=60, bg='#fff',activebackground='#fff',bd=0, relief='flat',
                                       command=self.cur)
                  self.backbt.place(x=5, y=5)
                  self.log = PhotoImage(file='back.png')
                  self.backbt.config(image=self.log, compound=LEFT)
                  self.small_log = self.log.subsample(1, 1)
                  self.backbt.config(image=self.small_log)

              def check(self):
                  self.ai=self.em.get()
                  self.b=self.em2.get()
                  cursor=dc.cursor()
                  cursor.execute("SELECT * FROM student WHERE Roll_no='"+self.ai+"' or ERP_ID='"+self.b+"'")
                  self.var=cursor.fetchone()
                  if self.var!=None:
                    if self.ai and not self.b:
                        self.em2.delete(0, END) 
                        self.em2.insert(0, self.var[0])

                    self.lb1=Label(self.fmi,text='Name :',fg='black',font=('Arial',10,'bold'))
                    self.lb1.place(x=60,y=255)
                    self.lb2 = Label(self.fmi, text=self.var[1], fg='black', font=('Arial', 10, 'bold'))
                    self.lb2.place(x=130, y=255)
                    self.lb3 = Label(self.fmi, text='Course :',fg='black', font=('Arial', 10, 'bold'))
                    self.lb3.place(x=60, y=275)
                    self.lb4 = Label(self.fmi, text=self.var[2],fg='black', font=('Arial', 10, 'bold'))
                    self.lb4.place(x=130, y=275)
                    self.lb5 = Label(self.fmi, text='Year :', fg='black', font=('Arial', 10, 'bold'))
                    self.lb5.place(x=60, y=295)
                    self.lb6 = Label(self.fmi, text=self.var[3], fg='black', font=('Arial', 10, 'bold'))
                    self.lb6.place(x=130, y=295)
                    self.lb7 = Label(self.fmi, text='Contact :', fg='black', font=('Arial', 10, 'bold'))
                    self.lb7.place(x=60, y=315)
                    self.lb8 = Label(self.fmi, text=self.var[6],fg='black', font=('Arial', 10, 'bold'))
                    self.lb8.place(x=130, y=315)
                    self.lb9 = Label(self.fmi, text='College :', fg='black', font=('Arial', 10, 'bold'))
                    self.lb9.place(x=60, y=335)
                    self.lb10 = Label(self.fmi, text=self.var[7],fg='black', font=('Arial', 10, 'bold'))
                    self.lb10.place(x=130, y=335)

                    self.fr=Frame(self.fmi,bg='#fff',bd=5,relief='flat',width=450,height=320)
                    self.fr.place(x=420,y=20)
                    self.ff=Frame(self.fr,bg='#0f624c',bd=2,relief='flat',width=450,height=35)
                    self.ff.place(x=0,y=0)
                    self.lb=Label(self.ff,text='ISSUE BOOK',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
                    self.lb.place(x=165,y=5)
                    self.tt=Label(self.fr,text='Book-ID',bg='#fff',fg='black',font=('arial',10,'bold'))
                    self.tt.place(x=50,y=60)
                    self.e1 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                    self.e1.place(x=160, y=60)
                    self.ttp = Label(self.fr, text='Title', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                    self.ttp.place(x=50, y=110)
                    self.e2 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                    self.e2.place(x=160, y=110)
                    self.bt1 = Button(self.fr, text='Submit', width=35, bg='#0f624c', fg='#fff', font=('Arial', 10,
                                                                    'bold'),bd=5,relief='flat',command=self.data)
                    self.bt1.place(x=60, y=160)

                    '''self.bt1 = Button(self.fr, text='Clear', width=13, bg='blue', fg='#fff', font=('Arial', 10,
                                                                                                  'bold'), bd=5,
                                relief='flat', command=self.clr1)
                    self.bt1.place(x=215, y=160)'''
                  else:
                       messagebox.showwarning('Warning','These Student are not Registered !')


              def clr(self):
                  self.em.delete(0, END)
                  self.em2.delete(0, END)
              '''def clr1(self):
                  self.e1.delete(0,END)
                  self.e2.delete(0,END)
                  self.boot.destroy()
                  self.data()'''


              def data(self):
                   self.vva=self.e1.get()
                   self.vvb=self.e2.get()
                   cursor=dd.cursor()
                   cursor.execute("SELECT * FROM stbook WHERE Book_ID='"+self.vva+"' and Title='"+self.vvb+"'")

                   dd.commit()
                   self.value=cursor.fetchone()
                   if self.value!=None:
                        if self.max==0:
                              self.boot=Tk()
                              self.boot.title("Issue Books")
                              self.boot.iconbitmap("lib.ico")
                              self.boot.configure(bg='#fff')
                              self.boot.geometry("300x660+600+50")
                              self.boot.resizable(0,0)

                              self.lb=Label(self.boot,text='Title',bg='#fff',fg='black',font=('Arial',10,'bold'))
                              self.lb.place(x=20,y=20)
                              self.lbn = Label(self.boot, text=self.value[1], bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                              self.lbn.place(x=110,y=20)
                              self.lb = Label(self.boot, text='Author', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lb.place(x=20, y=50)
                              self.lbn = Label(self.boot, text=self.value[2], bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=110, y=50)
                              self.lb = Label(self.boot, text='Edition', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lb.place(x=20, y=80)
                              self.lbn = Label(self.boot, text=self.value[3], bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=110, y=80)
                              self.plan = Label(self.boot, text='---------------------------------------------------',
                                        bg='#fff')
                              self.plan.place(x=5, y=110)
                              self.planx = Label(self.boot, text='---------------------------------------------------',
                                        bg='#fff')

                              self.planx.place(x=5, y=230)
                              self.planx = Label(self.boot, text='---------------------------------------------------',
                                        bg='#fff')

                              self.planx.place(x=5, y=350)

                        if self.max==1:

                              self.lbt = Label(self.boot, text='Title', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbt.place(x=20, y=140)
                              self.lbnt = Label(self.boot, text=self.value[1], bg='#fff', fg='black', font=('Arial',
                                                                                                            10, 'bold'))
                              self.lbnt.place(x=110, y=140)
                              self.lbtd = Label(self.boot, text='Author', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbtd.place(x=20, y=170)
                              self.lbn = Label(self.boot, text=self.value[2], bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=110, y=170)
                              self.lbc = Label(self.boot, text='Edition', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbc.place(x=20, y=200)
                              self.lbn = Label(self.boot, text=self.value[3], bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=110, y=200)

                        if self.max==2:

                              self.lbt = Label(self.boot, text='Title', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbt.place(x=20, y=260)
                              self.lbnt = Label(self.boot, text=self.value[1], bg='#fff', fg='black', font=('Arial',
                                                                                                            10, 'bold'))
                              self.lbnt.place(x=110, y=260)
                              self.lbtd = Label(self.boot, text='Author', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbtd.place(x=20, y=290)
                              self.lbn = Label(self.boot, text=self.value[2], bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=110, y=290)
                              self.lbc = Label(self.boot, text='Edition', bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbc.place(x=20, y=320)
                              self.lbn = Label(self.boot, text=self.value[3], bg='#fff', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=110, y=320)


                        if self.max>=3:
                              messagebox.showerror('Library System','Sorry,At Once Maximum 3 books can be issued!')


                        self.label = Label(self.fr, text='ADD MORE BOOKS ', bg='#fff', fg='black', font=('arial', 10,
                                                                                                    'bold'))
                        self.label.place(x=60, y=220)


                        #---------------------------------Radio Button-------------------------

                        self.radio_var = IntVar(value=2) 
                        self.it1=Radiobutton(self.fr,text='YES',bg='#fff',variable=self.radio_var,value=1,command=self.yes)
                        self.it1.place(x=210,y=220)

                        self.it2 = Radiobutton(self.fr, text='NO',bg='#fff', variable=self.radio_var, value=2,command=self.no)
                        self.it2.place(x=280, y=220)

                        #ISSUED button
                        self.button1 = Button(self.boot, text='Issued', bg='red', fg='#fff', width=30, height=0,
                                              font=('Arial', 8, 'bold'), command=self.issued)
                        self.button1.place(x=30, y=596)

                        #-----------------------date module uses-------------------------


                        self.today= date.today()


                        self.cal = Calendar(self.boot, selectmode="day", bg='black',year=self.today.year,month=self.today.month,day=self.today.day)
                        self.cal.place(x=20,y=370)


                        btn1 = Button(self.boot, text="Confirm Date",command=self.get_data,  bg='#ff0076',
                                      font=('arial', 10,'bold'),
                                      fg='#fff', relief='flat')
                        btn1.place(x=90,y=565)


                        self.boot.mainloop()

                   else:
                        messagebox.showwarning('Warning','YOUR DATA IS NOT FOUND !')


              def get_data(self):
                  self.datecon=self.cal.selection_get()


              def yes(self):

                    self.n=self.n+1
                    self.bt1 = Button(self.fr, text='Submit', width=35, bg='#0f624c', fg='#fff', font=('Arial', 10,
                                                        'bold'), bd=5,relief='flat',command=self.data, state=ACTIVE)
                    self.bt1.place(x=60, y=160)
                    self.bt1.configure(state=ACTIVE)

                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.max=self.max+1


              def no(self):

                    self.bt1 = Button(self.fr, text='Submit', width=35, bg='#0f624c', fg='#fff', font=('Arial', 10,
                                                   'bold'), bd=5,relief='flat',state=DISABLED)
                    self.bt1.place(x=60, y=160)
                    self.bt1.configure(state=DISABLED)


             

              def issued(self):
                  try:
                      # Retrieve the ERP ID and book id from the entry field
                      erp_id = self.em2.get()
                      from_date = self.cal.get_date() #MM/DD/YY
                      selected_date = datetime.strptime(from_date, "%m/%d/%y") 
                      today_date = datetime.now().date()

                      if selected_date.date() < today_date:
                        messagebox.showerror("Invalid Date", "Issue date cannot be in the past.")
                        return
                    
                      from_date = selected_date.strftime("%Y-%m-%d")
                      to_date = (selected_date + timedelta(days=10)).strftime("%Y-%m-%d")  # Due date
                        
                        # Update the database to record the book issuance and dates
                      cursor = dc.cursor()
                      cursor.execute("SELECT Issued_Books, From_date, To_date FROM student WHERE ERP_ID = ?", (erp_id,))
                      student_data = cursor.fetchone()
                      if not student_data:
                        messagebox.showerror("Error", "Student record not found.")
                        return
                     
                      issued_books, current_from_date, current_to_date = student_data
                      issued_books = issued_books if issued_books else ""
                      issued_books_set = set(issued_books.split(',')) if issued_books else set()

                      # Check if the book is already issued by this student
                      if self.vva in issued_books_set:
                        messagebox.showerror("Error", "This student already issued this book.")
                        return
                      
                      # Add the new book to the issued list
                      issued_books_set.add(self.vva)
                      updated_issued_books = ','.join(issued_books_set)


                     # Update `From_date` and `To_date` only if empty
                      if not current_from_date and not current_to_date:
                        cursor.execute(
                            """
                            UPDATE student
                            SET Issued_Books = ?, From_date = ?, To_date = ?, No_book = No_book + 1
                            WHERE ERP_ID = ?
                            """,
                            (updated_issued_books, from_date, to_date, erp_id)
                        )
                      else:
                        cursor.execute(
                            """
                            UPDATE student
                            SET Issued_Books = ?,From_date = ?, To_date = ?, No_book = No_book + 1
                            WHERE ERP_ID = ?
                            """,
                            (updated_issued_books,from_date, to_date, erp_id)
                        )

                      dc.commit()

                      # working on stbook
                      cursor_=dd.cursor()
                      cursor_.execute("SELECT ID, copies_available FROM stbook WHERE Book_ID = ?", (self.vva,))
                      result = cursor_.fetchone()
                    
                      if result:
                        current_issuers, copies_available = result
                        current_issuers = current_issuers if current_issuers else ""
                        updated_ids = set(current_issuers.split(',')) if current_issuers else set()
                        erp_id_str = str(erp_id)
                        if erp_id_str in updated_ids:
                            messagebox.showerror("Error", "This student already issued the book.")
                            return

                        # Update IDs and decrease available copies
                        updated_ids.add(erp_id_str)
                        updated_ids_str = ','.join(updated_ids)

                        if copies_available <= 0:
                            messagebox.showerror("Error", "No copies available for this book.")
                            return
                        
                        copies_available -= 1

                        # Update book status
                        issue_status = "Not Available" if copies_available == 0 else "Available"
                        cursor_.execute(
                            """
                            UPDATE stbook
                            SET Issue = ?, ID = ?, copies_available = ?
                            WHERE Book_ID = ?
                            """,
                            (issue_status, updated_ids_str, copies_available, self.vva)
                        )
                      dd.commit()
                      
                      # 
                      messagebox.showinfo("Library System", "Book issued successfully!")
                      print("from date:",from_date)
                      print("to date:",to_date)
                      
                      self.mail(erp_id)

                  except Exception as e:
                    print(f"Error issuing book: {e}")
                    messagebox.showerror("Error", f"Failed to issue book: {e}")

              def mail(self, erp_id):
                   try:
                        # Query the database for student details
                        cursor = dc.cursor()
                        cursor.execute("SELECT * FROM student WHERE ERP_ID=?", (erp_id,))
                        student_data = cursor.fetchone()

                        # Check if the student exists
                        if not student_data:
                            messagebox.showerror("Error", "No student found with the given ERP ID.")
                            return

                        # Extract student details
                        student_email = student_data[5] 
                        student_name = student_data[1]  
                        issued_books = student_data[13]
                        latest_book_id = issued_books.split(",")[-1] if issued_books else None
                        if not latest_book_id:
                            messagebox.showerror("Error", "No issued book found for the student.")
                            return

                        cursor_store = dd.cursor()
                        cursor_store.execute("SELECT Title FROM stbook WHERE Book_ID=?", (latest_book_id,))
                        book_data = cursor_store.fetchone()

                        if not book_data:
                            messagebox.showerror("Error", "Book details not found.")
                            return
                        
                        book_name = book_data[0]
                        # Sender's email and credentials
                        sender_email = "librarysystem5375121@gmail.com" #replace with your sender email
                        with open("pass.txt", 'r') as file:   #replace with your sender's app password
                            sender_password = file.read().strip()

                        # dates
                        issue_date = student_data[8]  
                        due_date = student_data[9]
                        issue_date_formatted = datetime.strptime(issue_date, "%Y-%m-%d").strftime("%d-%m-%Y")
                        due_date_formatted = datetime.strptime(due_date, "%Y-%m-%d").strftime("%d-%m-%Y")

                        # Construct the email body
                        email_body = (
                            f"Hi {student_name},\n\n"
                            f"The book *{book_name}* has been issued to you.\n"
                            f"Issue Date: {issue_date_formatted}\n"
                            f"Due Date: {due_date_formatted}\n\n"
                            "Please return the book by the due date to avoid fines.\n\n"
                            "Best regards,\nLibrary Department"
                        )

                        from email.mime.text import MIMEText
                        message = MIMEText(email_body)
                        message["Subject"] = "Library Department - Book Issued"
                        message["From"] = sender_email
                        message["To"] = student_email

                        # Send the email using SMTP
                        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        server.login(sender_email, sender_password)
                        server.sendmail(sender_email, student_email, message.as_string())
                        print(f"Email sent successfully to {student_email}.")
                        messagebox.showinfo("Library System", f"Email sent successfully to {student_name}!")

                   except Exception as e:
                    print(f"Error sending email: {e}")
                    messagebox.showerror("Error", f"Failed to send email: {e}")

                   finally:
                        try:
                             server.quit()
                        except Exception as cleanup_error:
                            print(f"Error during cleanup: {cleanup_error}")


         obk=test()
         obk.issue()



     def edit(self):
         class editing(maincode):
               def edbooks(self):


                     self.ffm=Frame(root,bg='#a7ecd9',width=900,height=390)
                     self.ffm.place(x=0,y=110)
                     self.bg_image = Image.open('bg10.png')  
                     self.bg_image = self.bg_image.resize((900, 390), Image.LANCZOS) 
                     self.bg_photo = ImageTk.PhotoImage(self.bg_image) 
                     self.bg_label = Label(self.ffm, image=self.bg_photo)
                     self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                     self.fm1 = Frame(self.ffm, bg='#fff', width=500, height=200, bd=5, relief='flat')
                     self.fm1.place(x=200, y=15)
                     self.ed = Frame(self.fm1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                     self.ed.place(x=0,y=0)
                     self.lab = Label(self.ed, text='EDIT BOOKS DETAILS', bg='#0f624c', fg='#fff', font=('Arial', 12,
                                                                                                    'bold'))
                     self.lab.place(x=165, y=5)
                     self.label3=Label(self.fm1,text='Book ID',bg='#fff',fg='black',font=('arial',10,'bold'))
                     self.label3.place(x=85,y=65)
                     self.entry=Entry(self.fm1,width=30,bd=4,relief='groove',font=('arial',8,'bold'))
                     self.entry.place(x=188,y=65)
                     self.button7 = Button(self.fm1, text='Search', bg='#0f624c', fg='#fff', width=24, height=0,
                                  font=('Arial', 10, 'bold'),command=self.search)
                     self.button7.place(x=140,y=120)

                     self.backbt = Button(self.ffm, width=60, bg='#a7ecd9',activebackground='#a7ecd9',
                                          bd=0, relief='flat', command=self.cur)
                     self.backbt.place(x=0, y=0)
                     self.log = PhotoImage(file='back.png')
                     self.backbt.config(image=self.log, compound=LEFT)
                     self.small_log = self.log.subsample(1, 1)
                     self.backbt.config(image=self.small_log)


                #----------------------Database----------------------------------


               def search(self):
                     self.datas=self.entry.get()
                     cursor=dd.cursor()
                     cursor.execute("SELECT * FROM stbook WHERE Book_ID='"+self.datas+"'" )
                     dd.commit()
                     self.val=cursor.fetchone()
                     if self.val!=None:

                          self.edcat=Tk()
                          self.edcat.title("Library System")
                          self.edcat.geometry("300x320+590+320")
                          self.edcat.configure(bg='#fff')
                          self.edcat.iconbitmap("lib.ico")


                          self.fc=Frame(self.edcat,bg='#0f624c',width=300,height=30)
                          self.fc.place(x=0,y=0)
                          self.lab=Label(self.fc,bg='#0f624c',fg='#fff',text='EDIT BOOKS',font=('arial',10,'bold'))
                          self.lab.place(x=112,y=5)
                          self.labid = Label(self.edcat, bg='#fff', fg='black', text='Book ID', font=('arial', 10,
                                                                                                    'bold'))
                          self.labid.place(x=30, y=45)
                          self.labti = Label(self.edcat, bg='#fff', fg='black', text='Title', font=('arial', 10,
                                                                                                    'bold'))
                          self.labti.place(x=30, y=90)
                          self.labaut = Label(self.edcat, bg='#fff', fg='black', text='Author', font=('arial', 10,
                                                                                                    'bold'))
                          self.labaut.place(x=30, y=135)
                          self.labed = Label(self.edcat, bg='#fff', fg='black', text='Edition', font=('arial', 10,
                                                                                                    'bold'))
                          self.labed.place(x=30, y=180)
                          self.labpr = Label(self.edcat, bg='#fff', fg='black', text='Price', font=('arial', 10,
                                                                                                    'bold'))
                          self.labpr.place(x=30, y=225)

                         #------------------------------Entry------------------------


                          self.en1=Entry(self.edcat,width=25,bd=4,relief='groove',font=('arial',8,'bold'))
                          self.en1.place(x=100,y=45)
                          self.en2 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en2.place(x=100, y=90)
                          self.en3 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en3.place(x=100, y=135)
                          self.en4 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en4.place(x=100, y=180)
                          self.en5 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en5.place(x=100, y=225)
                          self.butt = Button(self.edcat, text='Submit', bg='#0f624c', fg='#fff', width=20, height=0,
                                      font=('Arial', 10, 'bold'),command=self.savedit)
                          self.butt.place(x=67, y=270)

                         # -------------------insert value within edcat windows--------------------

                          self.en1.insert(0, self.val[0])
                          self.en2.insert(0, self.val[1])
                          self.en3.insert(0, self.val[2])
                          self.en4.insert(0, self.val[3])
                          self.en5.insert(0, self.val[4])

                          self.edcat.mainloop()

                     else:
                          messagebox.showerror('Library System','PLEASE! CORRECT BOOK ID')

                #-----------------BOKK is Updated-----------------


               def savedit(self):
                     self.id = self.en1.get()
                     self.ti = self.en2.get()
                     self.au = self.en3.get()
                     self.ed = self.en4.get()
                     self.pi = self.en5.get()

                     cursor= dd.cursor()
                     cursor.execute("UPDATE stbook SET Book_ID='"+self.id+"', Title='"+self.ti+"',Author='"+self.au+"',Edition='"+self.ed+"',Price='"+self.pi+"' WHERE Book_ID='"+self.datas+"'")
                     dd.commit()
                     messagebox.showinfo('Library System','YOUR DATA IS UPDATED!')

                     self.edcat.destroy()

         obj=editing()
         obj.edbooks()

         # -----------------------------------------------------------------------------------------------------


         # ------------------------------Return Book--------------------------------------------------
     def return_book(self):
         class retu(maincode):

             def __init__(self):
                self.frame = Frame(root, bd=0, relief='flat', bg='#a7ecd9', width=900, height=390)
                self.frame.place(x=0, y=110)

                self.bg_image = Image.open('bg77.png')  
                self.bg_image = self.bg_image.resize((900, 390), Image.LANCZOS) 
                self.bg_photo = ImageTk.PhotoImage(self.bg_image) 
                self.bg_label = Label(self.frame, image=self.bg_photo)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                
                self.f1 = Frame(self.frame, bg='#fff', width=500, height=200, bd=5, relief='flat')
                self.f1.place(x=200, y=15)
                self.ed = Frame(self.f1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                self.ed.place(x=0, y=0)
                self.lac = Label(self.ed, text='RETURN BOOKS ', bg='#0f624c', fg='#fff', font=('Arial', 12, 'bold'))
                self.lac.place(x=175, y=5)
                self.label8 = Label(self.f1, text='ERP ID', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                self.label8.place(x=85, y=65)
                self.entry4 = Entry(self.f1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                self.entry4.place(x=188, y=65)
                self.button9 = Button(self.f1, text='Return', bg='#0f624c', fg='#fff', width=24, height=0,
                                    font=('Arial', 10, 'bold'), command=self.retbook)
                self.button9.place(x=140, y=120)

                self.backbt = Button(self.frame, width=60, bg='#a7ecd9', activebackground='#a7ecd9',
                                    bd=0, relief='flat', command=self.cur)
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file='back.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(1, 1)
                self.backbt.config(image=self.small_log)

             def retbook(self):
                erp_id = self.entry4.get()  # Get ERP ID from the input field

                # Retrieve student data
                cursor = dc.cursor()
                cursor.execute("SELECT From_date, To_date, No_book, Issued_Books FROM student WHERE ERP_ID=?", (erp_id,))
                student_data = cursor.fetchone()

                if not student_data:
                    messagebox.showwarning("Library System", "Your ERP_ID is not found!")
                    return

                from_date_str, to_date_str, no_books, issued_books = student_data
                issued_books = issued_books.split(",") if issued_books else []

                if not issued_books:
                    messagebox.showerror("Error", "No books are currently issued to this ERP ID.")
                    return

                # Show checkbox selection for books
                self.checkbox_popup(erp_id, issued_books, from_date_str, to_date_str)

             def checkbox_popup(self, erp_id, issued_books, from_date_str, to_date_str):
                self.selection_window = Toplevel()
                self.selection_window.title("Select Books to Return")
                self.selection_window.geometry("300x300+590+348")
                self.selection_window.iconbitmap("lib.ico")
                self.selection_window.resizable(0, 0)
                self.selection_window.configure(bg="#74b2c2")

                Label(self.selection_window, text="Select books to return:",font=("Verdana", 12, "bold"),bg="#f5f5f5",fg="#333",).pack(pady=15)

                self.selected_books = {}
                for book in issued_books:
                    var = BooleanVar()
                    self.selected_books[book] = var
                    Checkbutton(self.selection_window, text=book, variable=var,font=("Arial", 10),bg="#f5f5f5",fg="#444",
                                activebackground="#d9f9f5",activeforeground="#000",selectcolor="#a7ecd9",).pack(anchor="w", padx=30, pady=5)

                Button(self.selection_window, text="Return Selected", command=lambda: self.process_multiple_returns(erp_id, from_date_str, to_date_str),
                       font=("Arial", 12, "bold"),bg="#0f624c",fg="white",activebackground="#13a895",activeforeground="white",width=20,height=2,
                       relief="raised",bd=3,).pack(pady=20)

             def process_multiple_returns(self, erp_id, from_date_str, to_date_str):
                self.selection_window.destroy()

                # Calculate fines and update records for selected books
                from_date = datetime.strptime(from_date_str, "%Y-%m-%d").date()
                to_date = datetime.strptime(to_date_str, "%Y-%m-%d").date()
                submit_date = date.today()

                fine_total = 0
                returned_books = []

                for book, var in self.selected_books.items():
                    if var.get():  # Check if book is selected
                        returned_books.append(book)

                        # Calculate fine for this book
                        fine = 0
                        if submit_date > to_date:
                            overdue_days = (submit_date - to_date).days
                            fine = 2 + (overdue_days * 2)  # Rs. 2 per book + Rs. 2 per overdue day
                        fine_total += fine

                # Update database
                cursor = dc.cursor()
                cursor.execute("SELECT Issued_Books FROM student WHERE ERP_ID=?", (erp_id,))
                result = cursor.fetchone()
                if result:
                    issued_books = result[0].split(",") if result[0] else []
                else:
                    issued_books = []
                updated_books = [book for book in issued_books if book not in returned_books]
                issued_books_str = ",".join(updated_books)
                no_books_remaining = len(updated_books)
                from_date_str = "" if no_books_remaining == 0 else from_date_str
                to_date_str = "" if no_books_remaining == 0 else to_date_str

                cursor.execute("""
                    UPDATE student
                    SET No_book = ?, From_date = ?, To_date = ?,submit_date = ?, Issued_Books = ?
                    WHERE ERP_ID = ?
                """, (no_books_remaining, from_date_str, to_date_str,submit_date.strftime("%Y-%m-%d"), issued_books_str, erp_id))
                dc.commit()

                # Update `stbook` 
                cursor_ = dd.cursor()
                for book in returned_books:
                    for book in returned_books:
                        cursor_.execute("SELECT ID FROM stbook WHERE Book_ID = ?", (book,))
                        result = cursor_.fetchone()

                        if result:
                            current_ids = result[0]  # Comma-separated ERP IDs
                            current_ids_set = set(current_ids.split(",")) if current_ids else set()

                            current_ids_set.discard(erp_id)

                            updated_ids = ",".join(current_ids_set)

                            # Determine the availability status
                            cursor_.execute(
                                """
                                UPDATE stbook
                                SET Issue = ?, ID = ?, Copies_Available = Copies_Available + 1
                                WHERE Book_ID = ?
                                """,
                                ("Available" if updated_ids == "" else "Not Available", updated_ids if updated_ids else None, book)
                            )

                dd.commit()

                # Display success message with total fine
                messagebox.showinfo("Success", f"Books returned successfully.\nTotal Fine: Rs. {fine_total}")

                 

         object=retu()

     #-----------------------------------------------------------------------------------------------


     #-------------------------------------Delete Books---------------------------------------------

     def delete(self):
         class dele(maincode):
               def deleteee(self):
                     self.ff = Frame(root, bg='#a7ecd9', width=900, height=390)
                     self.ff.place(x=0, y=110)
                     #bg image
                     self.bg_image = Image.open('bg3.png')  
                     self.bg_image = self.bg_image.resize((900, 390), Image.LANCZOS) 
                     self.bg_photo = ImageTk.PhotoImage(self.bg_image) 
                     self.bg_label = Label(self.ff, image=self.bg_photo)
                     self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

                     self.f1 = Frame(self.ff, bg='#fff', width=500, height=200, bd=5, relief='flat')
                     self.f1.place(x=200, y=15)
                     self.ed = Frame(self.f1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                     self.ed.place(x=0, y=0)
                     self.lac = Label(self.ed, text='DELETE BOOKS ', bg='#0f624c', fg='#fff', font=('Arial', 12,'bold'))
                     self.lac.place(x=175, y=5)
                     self.label8 = Label(self.f1, text='Book ID', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                     self.label8.place(x=85, y=65)
                     self.entry4 = Entry(self.f1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                     self.entry4.place(x=188, y=65)
                     self.button9 = Button(self.f1, text='Delete', bg='#0f624c', fg='#fff', width=24, height=0,
                                  font=('Arial', 10, 'bold'),command=self.deldata)
                     self.button9.place(x=140, y=120)

                     self.backbt = Button(self.ff,width=60, bg='#a7ecd9',activebackground='#a7ecd9',
                                          bd=0, relief='flat', command=self.cur)
                     self.backbt.place(x=0, y=0)
                     self.log = PhotoImage(file='back.png')
                     self.backbt.config(image=self.log, compound=LEFT)
                     self.small_log = self.log.subsample(1, 1)
                     self.backbt.config(image=self.small_log)


               def deldata(self):
                     self.a=self.entry4.get()
                     cursor=dd.cursor()
                     cursor.execute("DELETE FROM stbook WHERE Book_ID='"+self.a+"'")
                     dd.commit()
                     self.da=cursor.fetchone()
                     if self.da!=None:
                          messagebox.showinfo('Library System','Requested Book Deleted successfully!')
                     else:
                          messagebox.showerror('Library System','YOUR DATA IS NOT FOUND !')

         occ=dele()
         occ.deleteee()

     #------------------------------------------------------------------------------------------------


     #---------------------------------------Search Books---------------------------------------------

     def search(self):
         class demt(maincode):
             def delmdata(self):

                 self.fc = Frame(root, bg='#a7ecd9', width=900, height=390)
                 self.fc.place(x=0, y=110)
                 #bg image
                 self.bg_image = Image.open('bg2.png')  
                 self.bg_image = self.bg_image.resize((900, 390), Image.LANCZOS) 
                 self.bg_photo = ImageTk.PhotoImage(self.bg_image) 
                 self.bg_label = Label(self.fc, image=self.bg_photo)
                 self.bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

                 self.fc1 = Frame(self.fc, bg='#fff', width=500, height=200, bd=5, relief='flat')
                 self.fc1.place(x=200, y=15)
                 self.edm = Frame(self.fc1, bg='#0f624c', bd=0, relief='flat', width=490, height=35)
                 self.edm.place(x=0, y=0)
                 self.lac = Label(self.edm, text='SEARCH BOOKS ', bg='#0f624c', fg='#fff', font=('Arial', 12, 'bold'))
                 self.lac.place(x=175, y=5)
                 self.label8 = Label(self.fc1, text='Book ID', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label8.place(x=85, y=65)
                 self.entryl= Entry(self.fc1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entryl.place(x=188, y=65)
                 self.butto = Button(self.fc1, text='Search', bg='#0f624c', fg='#fff', width=24, height=0,
                                       font=('Arial', 10, 'bold'),command=self.srch)
                 self.butto.place(x=140, y=120)

                 self.backbt = Button(self.fc,width=60, bg='#a7ecd9',activebackground='#a7ecd9',bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)


             def srch(self):
                 self.emp=self.entryl.get()
                 cursor=dd.cursor()
                 cursor.execute("SELECT * FROM stbook WHERE Book_ID='"+self.emp+"'")
                 dd.commit()
                 self.srval=cursor.fetchone()
                 if self.srval!=None:

                     self.top=Tk()
                     self.top.title("Library System")
                     self.top.iconbitmap("lib.ico")
                     self.top.geometry("300x300+600+300")
                     self.top.resizable(0, 0)
                     self.top.configure(bg='#fff')

                     self.frm=Frame(self.top,bg='#0f624c',width=300,height=35)
                     self.frm.place(x=0,y=0)

                     self.mnlb=Label(self.frm,bg='#0f624c',fg='#fff',text="Avaliable",font=('arial',11,'bold'))
                     self.mnlb.place(x=120,y=5)

                     self.lb1 = Label(self.top, text='Title', bg='#fff', fg='black', font=('arial', 12, 'bold'))
                     self.lb1.place(x=40,y=80)
                     self.lb2=Label(self.top,text=self.srval[1],bg='#fff',fg='black',font=('arial',12,'bold'))
                     self.lb2.place(x=120,y=80)

                     self.lb3 = Label(self.top, text='Author', bg='#fff', fg='black', font=('arial', 12, 'bold'))
                     self.lb3.place(x=40, y=160)
                     self.lb4 = Label(self.top, text=self.srval[2], bg='#fff', fg='black', font=('arial', 12, 'bold'))
                     self.lb4.place(x=120, y=160)

                     self.lb5 = Label(self.top, text='Edition', bg='#fff', fg='black', font=('arial', 12, 'bold'))
                     self.lb5.place(x=40, y=240)
                     self.lb6 = Label(self.top, text=self.srval[3], bg='#fff', fg='black', font=('arial', 12, 'bold'))
                     self.lb6.place(x=120, y=240)


                 else:
                     messagebox.showwarning('Library System','YOUR DATA IS NOT AVAILABLE !')

         object=demt()
         object.delmdata()

     #-----------------------------------------------------------------------------------------------------


    #-------------------------------------------SHOW BOOKS_------------------------------------------------

     def show(self):
         class tst(maincode):
             def __init__(self):
                 self.fc = Frame(root, bg='#a7ecd9', width=900, height=390)
                 self.fc.place(x=0, y=110)
                 self.popframe=Frame(self.fc,width=900,height=30,bg='#0f624c')
                 self.popframe.place(x=0,y=0)
                 self.lbn=Label(self.popframe,bg='#0f624c',text='BOOKS INFORMATION',fg='#fff',font=('arial',10,
                                                                                                      'bold'))
                 self.lbn.place(x=380,y=5)

                 self.backbt = Button(self.popframe,width=30, bg='#0f624c',activebackground='#0f624c',
                                      bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(2, 2)
                 self.backbt.config(image=self.small_log)


                 self.table_frame=Frame(self.fc,bg='#fff',bd=1,relief='flat')
                 self.table_frame.place(x=0,y=30,width=900,height=360)

                 self.scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
                 self.scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
                 self.book_table=ttk.Treeview(self.table_frame,columns=("Book ID","Title","Author","Edition",
                                                                           "Price","Status"),
                                      xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                 self.scroll_x.pack(side=BOTTOM,fill=X)
                 self.scroll_y.pack(side=RIGHT, fill=Y)
                 self.scroll_x.config(command=self.book_table.xview)
                 self.scroll_y.config(command=self.book_table.yview)

                 self.book_table.heading("Book ID",text="Book ID")
                 self.book_table.heading("Title", text="Title")
                 self.book_table.heading("Author", text="Author")
                 self.book_table.heading("Edition", text="Edition")
                 self.book_table.heading("Price", text="Price")
                 self.book_table.heading("Status", text="Status")

                 self.book_table['show']='headings'

                 self.book_table.column("Book ID",width=150)
                 self.book_table.column("Title", width=200)
                 self.book_table.column("Author", width=200)
                 self.book_table.column("Edition", width=100)
                 self.book_table.column("Price", width=100)
                 self.book_table.column("Status", width=100)
                 self.book_table.pack(fill=BOTH,expand=1)

                 self.fetch_data()

             def fetch_data(self):
                 cursor=dd.cursor()
                 cursor.execute("SELECT Book_ID, Title, Author, Edition, Price, Issue FROM stbook")
                 self.rows=cursor.fetchall()
                 if len(self.rows)!=0:
                      for self.row in self.rows:
                           self.book_table.insert('',END,values=self.row)
                 dd.commit()


         oc=tst()

     #-----------------------------------------------------------------------------------------


     #---------------------------------------LOGIN SYSTEM--------------------------------------

     def code(self):

         self.fm=Frame(root,height=500,width=900,bg='white')
         self.fm.place(x=0,y=0)

         self.canvas=Canvas(self.fm,height=500,width=900,bg='#22224b')
         self.canvas.place(x=0,y=0)

         # Load and resize the login image to fit the canvas
         login_image = Image.open("bg88.png")
         login_image = login_image.resize((900, 500), Image.LANCZOS)
         self.photo = ImageTk.PhotoImage(login_image)
         self.canvas.create_image(0,0,image=self.photo,anchor=NW)

         self.fm1=Frame(self.canvas,height=260,width=300,bg='white',bd=3,relief='ridge')
         self.fm1.place(x=300,y=170)

         self.photo1=PhotoImage(file="open.png")
         self.canvas.create_image(450,110,image=self.photo1,anchor=CENTER)


         self.b1=Label(self.fm1,text='User ID',bg='white',font=('Arial',10,'bold'))
         self.b1.place(x=20,y=42)

         self.e1=Entry(self.fm1,width=22,font=('arial',9,'bold'),bd=4,relief='groove')
         self.e1.place(x=100,y=40)

         self.lb2=Label(self.fm1,text='Password',bg='white',font=('Arial',10,'bold'))
         self.lb2.place(x=20,y=102)

         self.e2=Entry(self.fm1,width=22,show='*',font=('arial',9,'bold'),bd=4,relief='groove')
         self.e2.place(x=100,y=100)


         self.btn1=Button(self.fm1,text='  login',fg='white',bg='red',width=100,font=('Arial',11,'bold'),
                 activebackground='white',activeforeground='black',command=self.login,bd=3,relief='flat',cursor='hand2')
         self.btn1.place(x=25,y=160)
         self.logo = PhotoImage(file='user.png')
         self.btn1.config(image=self.logo, compound=LEFT)
         self.small_logo = self.logo.subsample(1, 1)
         self.btn1.config(image=self.small_logo)


         self.btn2=Button(self.fm1,text=' add user',fg='white',bg='blue',width=100,font=('Arial',10,'bold'),
                 activebackground='white',activeforeground='black',bd=3,relief='flat',cursor='hand2',
                          command=self.add_student)
         self.btn2.place(x=155,y=160)
         self.log = PhotoImage(file='add_user.png')
         self.btn2.config(image=self.log, compound=LEFT)
         self.small_log = self.log.subsample(1, 1)
         self.btn2.config(image=self.small_log)


         # Sign Up button for new admins
         self.btn3 = Button(self.fm1, text='  sign up', fg='white', bg='green', width=100, font=('Arial', 10, 'bold'),
                           activebackground='white', activeforeground='black', bd=3, relief='flat', cursor='hand2',
                           command=self.sign_up)  # Create a 'sign_up' function to handle sign-ups
         self.btn3.place(x=155, y=220)
         self.signup = PhotoImage(file='signup.png')
         self.btn3.config(image=self.signup, compound=LEFT)
         self.small_signup = self.signup.subsample(1, 1)
         self.btn3.config(image=self.small_signup)

         #-----------------------label clicked change password---------------------

         self.forgot=Label(self.fm1,text='forgot password!',fg='red',bg='#fff',activeforeground='black',
                           font=('cursive',9,'bold'))
         self.forgot.place(x=25,y=220)
         self.forgot.bind("<Button>",self.mouseClick)


         root.mainloop()

                        #------------------sign up window---------------------------
     def sign_up(self):
        self.signup_window = Toplevel(root)
        self.signup_window.title("Admin Sign Up")
        self.signup_window.geometry("400x450+530+200")
        self.signup_window.iconbitmap("lib.ico")
        self.signup_window.resizable(0, 0)
        self.signup_window.configure(bg='#090c36')

            # Title Label
        title_label = Label(self.signup_window, text="Admin Sign Up", bg='#090c36', fg='#d4f037', font=("Palatino", 20, 'bold'))
        title_label.place(x=105, y=15)

            #user name
        name_label = Label(self.signup_window, text='Name:', bg='#090c36', fg='#fff', font=("cursive", 10, 'bold'))
        name_label.place(x=40, y=70)
        self.new_name_entry = Entry(self.signup_window, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.new_name_entry.place(x=170, y=70)

            # User ID Label and Entry
        user_label = Label(self.signup_window, text='User ID:', bg='#090c36', fg='#fff', font=("cursive", 10, 'bold'))
        user_label.place(x=40, y=110)
        self.new_user_entry = Entry(self.signup_window, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.new_user_entry.place(x=170, y=110)

            # Password Label and Entry
        pass_label = Label(self.signup_window, text='Password:', bg='#090c36', fg='#fff', font=("cursive", 10, 'bold'))
        pass_label.place(x=40, y=150)
        self.new_password_entry = Entry(self.signup_window, width=24, show='*', font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.new_password_entry.place(x=170, y=150)

            # email label and entry
        email_label = Label(self.signup_window, text='Email:', bg='#090c36', fg='#fff', font=("cursive", 10, 'bold'))
        email_label.place(x=40, y=190)
        self.new_email_entry = Entry(self.signup_window, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.new_email_entry.place(x=170, y=190)

            #contact no. label
        contact_label = Label(self.signup_window, text='Contact No.:', bg='#090c36', fg='#fff', font=("cursive", 10, 'bold'))
        contact_label.place(x=40, y=230)
        self.new_contact_entry = Entry(self.signup_window, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.new_contact_entry.place(x=170, y=230)

            # Submit Button
        submit_button = Button(self.signup_window, text='Sign Up', fg='white', bg='#28a745', width=20, font=('Arial', 13, 'bold'),
                                activebackground='white', activeforeground='black', bd=3, relief='flat', cursor='hand2',
                                command=self.save_new_admin)
        submit_button.place(x=100, y=310)

     def save_new_admin(self):
        new_name = self.new_name_entry.get()
        new_user = self.new_user_entry.get()
        new_password = self.new_password_entry.get()
        new_email = self.new_email_entry.get()
        new_contact = self.new_contact_entry.get()

        # Check if fields are filled
        if not new_user or not new_password or not new_email or not new_contact:
             messagebox.showerror("Error", "Please fill all fields!")
             return

        # Save new admin to the database
        conn = sqlite3.connect('admin.db',timeout=10)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO adm (User_ID, Name, Password, email, phone_no) VALUES (?, ?, ?, ?, ?)", 
                   (new_user, new_name, new_password, new_email, new_contact))
        conn.commit()
        conn.close()

            # Show success message and close sign-up window
        messagebox.showinfo("Library System", "New admin registered successfully!")
        self.signup_window.destroy()


     def mouseClick(self,event):
         self.rog=Tk()
         self.rog.title("Change password")
         self.rog.geometry("400x300+530+200")
         self.rog.iconbitmap("lib.ico")
         self.rog.resizable(0,0)
         self.rog.configure(bg='#fff')

         self.label=Label(self.rog,text="New password",bg='#fff',fg='red',font=("cursive",20,'bold'))
         self.label.place(x=105,y=15)

         self.user=Label(self.rog,text='User ID :',bg='#fff',fg='black',font=("cursive",10,'bold'))
         self.user.place(x=40,y=95)

         self.user = Label(self.rog, text='New password :', bg='#fff', fg='black', font=("cursive", 10, 'bold'))
         self.user.place(x=40, y=170)

         self.e1 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e1.place(x=170, y=95)

         self.e2 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e2.place(x=170, y=170)

         self.btn1 = Button(self.rog, text='Submit', fg='white', bg='#5500ff', width=20, font=('Arial', 13, 'bold'),
                            activebackground='white', activeforeground='black',bd=3, relief='flat',
                            cursor='hand2',command=self.chan_pas)
         self.btn1.place(x=100, y=240)

     def chan_pas(self):
         self.a=self.e1.get()
         self.b=self.e2.get()
         conn=sqlite3.connect('admin.db')
         cursor=conn.cursor()
         cursor.execute("SELECT * FROM adm WHERE User_ID='"+self.a+"'")
         conn.commit()
         self.data=cursor.fetchone()

         if self.data!=None:
             cursor = conn.cursor()
             cursor.execute("UPDATE adm SET Password='" + self.b + "' WHERE User_ID='" + self.a + "'")
             conn.commit()
             messagebox.showinfo("Library System","Your Password is changed !")
             self.rog.quit()

         else:
             self.er = Label(self.rog, text='ID not found', bg='#fff', fg='red', font=("cursive", 8, 'bold'))
             self.er.place(x=170, y=125)
             self.rog.after(2000,self.rog.quit)

         self.rog.mainloop()

ob=maincode()
ob.code()
