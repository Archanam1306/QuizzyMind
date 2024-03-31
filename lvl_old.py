# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image

 
f=("Arial",25)
b=("Arial",15)

# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("1050x800")

master['bg']='lavender'

master.title('Level Page')
 
# function to open a new window
# on a button click
def Easy_quiz():
    master.destroy()
    import easy

def Medium_quiz():
    master.destroy()
    import medium

def Hard_quiz():
    master.destroy()
    import Hard

#Label text for instruction
instruction = Label(master, text = "CHOOSE THE LEVEL", font=f, bg='LightSteelBlue2')
instruction.grid(row=0, column=3, padx=400, pady=10)

# a button widget which will open a
# new window on button click
btn1 = Button(master,
             text ="Easy", command=Easy_quiz, font=b, activeforeground="red"
              , activebackground="pink",padx=15, pady=5, bg="floral white")
btn2 = Button(master,
             text ="Medium", command=Medium_quiz, font=b, activeforeground="red"
              , activebackground="pink", pady=5, bg="floral white")
btn3 = Button(master,
             text ="Hard", command=Hard_quiz, font=b, activeforeground="red"
              , activebackground="pink",padx=15, pady=5, bg="floral white")

btn1.grid(row=2, column=3, padx=150, pady=10)
btn2.grid(row=3, column=3, padx=150, pady=10)
btn3.grid(row=4, column=3, padx=150, pady=10)

# choosing the level
#instruction3 = Label(master, text = "CHOOSE THE LEVEL",bg='orange').grid(row=5,column=3, padx=500, pady=10)
# placing buttons
btn1.place(x=500,y=100)
btn2.place(x=500,y=200)
btn3.place(x=500,y=300)
# mainloop, runs infinitely
mainloop()
