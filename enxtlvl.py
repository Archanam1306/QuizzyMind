from tkinter import *
from tkinter.ttk import *
 
# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("1000x500")
 
 
# function to open a new window
# on a button click
def newlvl():
    master.destroy()
    import medium 

def quit_z():
    master.destroy()

instruction1 = Label(master, text = "Do you want to continue to next level?").grid(row=5,column=3, padx=400, pady=10)
btn1 = Button(master,
             text ="Yes",
             command = newlvl)
btn1.place(x=400,y=100)
btn1 = Button(master,
             text ="No",
             command = quit_z)
btn1.place(x=500,y=100)

mainloop()
