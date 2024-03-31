from tkinter import*
from PIL import ImageTk
import tkinter.messagebox as mb


 
f=("Arial",25)
b=("Arial",15)

master=Tk()
master.geometry('800x500')

bgImage=ImageTk.PhotoImage(file='level.jpg')
bgLabel=Label(master,image=bgImage)
bgLabel.place(x=0,y=0)
def Easy_quiz():
    master.destroy()
    import easy

def Medium_quiz():
    master.destroy()
    import medium

def Hard_quiz():
    master.destroy()
    import Hard


instruction = Label(master, text = "CHOOSE THE LEVEL", font=f)
instruction.grid(row=0, column=3, padx=250, pady=10)
btn1 = Button(master,
             text ="Easy", command=Easy_quiz, font=b, activeforeground="red"
              , activebackground="pink",padx=15, pady=5, bg="pale turquoise")

btn2 = Button(master,
             text ="Medium", command=Medium_quiz, font=b, activeforeground="red"
              , activebackground="pink", pady=5, bg="pale turquoise")
btn3 = Button(master,
             text ="Hard", command=Hard_quiz, font=b, activeforeground="red"
              , activebackground="pink",padx=15, pady=5, bg="pale turquoise")

btn1.grid(row=2, column=3, padx=150, pady=10)
btn2.grid(row=3, column=3, padx=150, pady=10)
btn3.grid(row=4, column=3, padx=150, pady=10)

# choosing the level
#instruction3 = Label(master, text = "CHOOSE THE LEVEL",bg='orange').grid(row=5,column=3, padx=500, pady=10)
# placing buttons
btn1.place(x=350,y=100)
btn2.place(x=350,y=250)
btn3.place(x=350,y=400)
master.mainloop()

