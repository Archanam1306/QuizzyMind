from tkinter import*
from PIL import ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc

#Functionality part
def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

    
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def clear():
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)

def connect_database():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        mb.showerror('Error','All Fields Are Required')
    else:
        c=mc.connect(host='localhost',user='root',password='india123',database='project')
        cur=c.cursor()
        q='insert into detailsnew(username,password) values(%s,%s)'
        cur.execute(q,(usernameEntry.get(),passwordEntry.get()))
        a='insert into details_with_score(username,password,score) values(%s,%s,0)'
        cur.execute(a,(usernameEntry.get(),passwordEntry.get()))
        c.commit()
        c.close()
        mb.showinfo('Success','Registered')
        clear()
        login_window.destroy()
        import instructionsnew

def show_leaderboard():
    import csv_leaderboard

def show_levelscreen():
    import lvl_old
        


    
login_window=Tk()
login_window.geometry('998x660+50+50')

bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold')
                  ,bg='white',fg='firebrick1')


heading.place(x=605,y=120)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold')
                    ,bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)


passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold')
                    ,bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')

eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=800,y=225)


loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white',
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=connect_database)
loginButton.place(x=578,y=300)

loginButton=Button(login_window,text='Leader Board',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white',
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=show_leaderboard)
loginButton.place(x=578,y=350)

loginButton=Button(login_window,text='Choose Level',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white',
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=show_levelscreen)
loginButton.place(x=578,y=400)
                    



login_window.mainloop()
