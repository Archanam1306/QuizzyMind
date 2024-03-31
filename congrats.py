from tkinter import*
from PIL import ImageTk
import tkinter.messagebox as mb


 
f=("Arial",15)
b=("Arial",10)

master=Tk()
master.geometry('800x450')

bgImage=ImageTk.PhotoImage(file='gameover.jpg')
bgLabel=Label(master,image=bgImage)
bgLabel.place(x=0,y=0)

def last():
    master.destroy()
def continue_h():
    master.destroy()
    import loginnewcopy


instruction = Label(master, text = "CONGRATULATIONS YOU HAVE COMPLETED THE QUIZ", font=f, bg='firebrick',fg='white')
instruction.grid(row=0, column=3, padx=120, pady=10)

instruction2 = Label(master, text = "CLICK HERE TO CONTINUE", font=f, bg='cyan')
instruction2.grid(row=1, column=3, padx=200, pady=30)
btn1 = Button(master,
             text ="Exit", command=last, font=b, activeforeground="red"
              , activebackground="pink",padx=15, pady=5, bg="IndianRed1")
btn2 = Button(master,
             text ="Continue", command=continue_h, font=b, activeforeground="red"
              , activebackground="pink", pady=5, bg="IndianRed1")

btn1.grid(row=2, column=3, padx=150, pady=10)
btn2.grid(row=3, column=3, padx=150, pady=10)


# choosing the level
#instruction3 = Label(master, text = "CHOOSE THE LEVEL",bg='orange').grid(row=5,column=3, padx=500, pady=10)
# placing buttons
btn1.place(x=100,y=100)
btn2.place(x=600,y=100)

master.mainloop()



