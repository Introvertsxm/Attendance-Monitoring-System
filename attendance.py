from tkinter import *
w=Tk()
w.geometry('1000x1000')
w.config(background='CADETBLUE')
w.title('Attendance Monitoring System by ~ SAMEER KHAN')
#img=PhotoImage(file='C:\\Users\\user\\OneDrive\\Documents\\python project\\Tkinter\\icons\\.png')
#w.iconphoto(False, img)
import sqlite3
try:
   db=sqlite3.connect('library_attendance.db')
   cr=db.cursor()
   cr.execute('create table login(name text, registration integer, date date, status boolean)')
   db.commit()
except:
    print('Database created successfully')

#Global variable to store data from the form
x=StringVar()#name
y=StringVar()#registration
u=StringVar()#date
v=StringVar()#status

l1=Label(w,text='ATTENDANCE FORM',font=('GEORGIA',30,'bold'),fg='black',bg='CADETBLUE')
l1.pack()

l2=Label(w,text='Name:',font=('GEORGIA',18,'bold'),bg='CADETBLUE',fg='black')
l2.place(x=30,y=120)

l3=Label(w,text='Registration:',font=('GEORGIA',18,'bold'),bg='CADETBLUE',fg='black')
l3.place(x=30,y=160)

l4=Label(w,text='Date:',font=('GEORGIA',18,'bold'),bg='CADETBLUE',fg='black')
l4.place(x=30,y=200)

l5=Label(w,text='Status:',font=('GEORGIA',18,'bold'),bg='CADETBLUE',fg='black')
l5.place(x=30,y=240)

#entry box:-
e1=Entry(w,font=('GEORGIA',20,'bold'))
e1.place(x=200,y=120)

e2=Entry(w,font=('GEORGIA',20,'bold'))
e2.place(x=200,y=160)

e3=Entry(w,font=('GEORGIA',20,'bold'))
e3.place(x=200,y=200)

e4=Entry(w,font=('GEORGIA',20,'bold'))
e4.place(x=200,y=240)


#button
def submit():
    a=x.get()
    b=y.get()
    c=u.get()
    d=v.get()
    cr.execute("insert into login(name, registration, date, status)values(?,?,?,?)",(a,b,c,d))
    db.commit()
b1=Button(w,text='Submit',font=('GEORGIA',15,'bold'),fg='black',bg='Seagreen',command=submit)
b1.place(x=150,y=300)

#clear
def clear():
    x.set('')
    y.set('')
    u.set('')
    v.set('')
b2=Button(w,text='Clear',font=('GEORGIA',15,'bold'),fg='black',bg='red',command=clear)
b2.place(x=270,y=300)

w.mainloop()
