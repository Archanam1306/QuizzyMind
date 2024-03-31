from tkinter import*
from PIL import ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc

#Functionality part
def hide():
    openeye.config(file='closeeye.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password.config(show='')
    eyeButton.config(command=hide)

    
def user_enter(event):
    if username.get()=='username':
        username.delete(0,END)
    if password.get()=='password':
        password.delete(0,END)
    if(username=="" or password==""):
            mb.showinfo('Insert data','All fields required')
            c=mc.connect(host='localhost',user='root',password='Avengers@98_',database='project')
            cur=c.cursor()
            q='insert into detailsnew(username,password)values(%s,%s)'
            cur.execute(q,(username.get(),password.get()))
            c.commit()
        
      
        
        
            mb.showinfo('Insert','Inserted successfully')
            c.close()


'''def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)'''

'''def insert():
    
    name=e_name.get()
    password=e_password.get()

  if( username=="" or password==""):
        mb.showinfo('Insert data','All fields required')
    else:
        c=mc.connect(host='localhost',user='root',password='Avengers@98_',database='project')
        cur=c.cursor()
        cur.execute("Insert into detailsnew values('"+username+"','"+password+"')")
        cur.execute("commit");
        
      
        username.delete(0, 'end')
        password.delete(0, 'end')
        
        mb.showinfo('Insert','Inserted successfully')
        c.close();'''

def lvl():
    login_window.destroy()
    import lvl

    
login_window=Tk()
login_window.geometry('998x660+50+50')

bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold')
                  ,bg='white',fg='firebrick1')


heading.place(x=605,y=120)

username=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold')
                    ,bd=0,fg='firebrick1')
username.place(x=580,y=200)
username.insert(0,'Username')
username.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)


password=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold')
                    ,bd=0,fg='firebrick1')
password.place(x=580,y=260)
password.insert(0,'Password')
password.bind('<FocusIn>',user_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')

eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=800,y=225)

'''insert=Button(login_window,text='Insert',font=('italic',13,'bold'),
              fg='white',bg='firebrick1',activeforeground='white',
              activebackground='firebrick1',cursor='hand2',command=insert)
insert.place(x=578,y=300)'''

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white',
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=lvl)
loginButton.place(x=578,y=350)
                    



login_window.mainloop()
