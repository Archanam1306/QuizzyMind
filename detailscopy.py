from tkinter import*
import tkinter.messagebox as mb
import mysql.connector as mc

def insert():
    id=e_id.get()
    name=e_name.get()
    password=e_password.get()

    if(id=="" or name=="" or password==""):
        mb.showinfo('Insert data','All fields required')
    else:
        c=mc.connect(host='localhost',user='root',password='',database='project')
        cur=c.cursor()
        cur.execute("Insert into details values('"+id +"','"+name+"','"+password+"')")
        cur.execute("commit");
        
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_password.delete(0, 'end')
        show()
        mb.showinfo('Insert','Inserted successfully')
        c.close();

def delete():
    if (e_id.get()==""):
        mb.showinfo('Delete','ID compulsory for deletion')
    else:
        c=mc.connect(host='localhost',user='root',password='',database='project')
        cur=c.cursor()
        cur.execute('delete from details where id="'+e_id.get()+'"')
        cur.execute('commit')

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_password.delete(0, 'end')
        show()
        mb.showinfo('Delete','Deleted successfully')
        c.close();

def update():
    id=e_id.get()
    name=e_name.get()
    password=e_password.get()

    if(id=="" or name=="" or password==""):
        mb.showinfo('Update status','All fields required')
    else:
        c=mc.connect(host='localhost',user='root',password='',database='project')
        cur=c.cursor()
        cur.execute("Update details set name='"+name+"','"+password+"'where id'"+id+"'")
        cur.execute("commit");
        
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_password.delete(0, 'end')
        show()
        mb.showinfo('Update','Updated successfully')
        c.close();

def get():
    if (e_id.get()==""):
        mb.showinfo('Fetch','ID compulsory')
    else:
        c=mc.connect(host='localhost',user='root',password='',database='project')
        cur=c.cursor()
        cur.execute("select * from details where id='"+e_id.get() +"'")
        rows=cur.fetchall()

        for row in rows:
            e_name.insert(0,row[1])
            e_password.insert(0,row[2])
        c.close();
def show():
    c=mc.connect(host='localhost',user='root',password='',database='project')
    cur=c.cursor()
    cur.execute("select * from details ")
    rows=cur.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData=str(row[0])+'        '+row[1]
        list.insert(list.size()+1, insertData)
    c.close(); 
    
def lvl():
    root.destroy()
    import lvl

root= Tk()
root.geometry("900x600")
root.title("DETAILS")

id=Label(root, text="ENTER ID",font=("bold",10))
id.place(x=30,y=40)

name=Label(root,text='Enter name',font=('bold',10))
name.place(x=30,y=80)

password=Label(root,text='Enter password',font=('bold',10))
password.place(x=30,y=120)

e_id=Entry()
e_id.place(x=150,y=30)

e_name=Entry()
e_name.place(x=150,y=70)

e_password=Entry()
e_password.place(x=150,y=110)

insert=Button(root,text='insert',font=('italic',10),bg='white',command=insert)
insert.place(x=30,y=150)

delete=Button(root,text='delete',font=('italic',10),bg='white',command=delete)
delete.place(x=100,y=150)

update=Button(root,text='update',font=('italic',10),bg='white',command=update)
update.place(x=170,y=150)

get=Button(root,text='get',font=('italic',10),bg='white',command=get)
get.place(x=240,y=150)

b=Button(root,text='Levels',font=('italic',10),bg='white',command=lvl)
b.place(x=300,y=150)

list=Listbox(root)
list.place(x=400,y=30)
show()

root.mainloop()



    
