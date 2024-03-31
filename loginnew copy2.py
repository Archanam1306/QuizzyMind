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
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19)
loginButton.place(x=578,y=300)
                    



login_window.mainloop()
