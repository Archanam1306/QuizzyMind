# and modules which are available in
# tkinter and ttk module
from tkinter import *
#from tkinter.ttk import *
from PIL import ImageTk, Image


f=("Arial",15)
b=("Arial",15)

# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("900x300")

master['bg']='lavender'

master.title('NextLevel Page')
 
# function to open a new window
# on a button click
def newlvl():
    master.destroy()
    import medium 

def quit_z():
    master.destroy()

#Label text for congrats
instruction = Label(master, text = "Do you want to continue to next level?", font=f, bg='LightSteelBlue2')
instruction.grid(row=0, column=3, padx=300, pady=10)

# new window on button click
btn1 = Button(master,
             text ="Yes", command=newlvl, font=b, activeforeground="red"
              , activebackground="pink",padx=15, pady=5, bg="floral white")
btn1.grid(row=2, column=3, padx=100, pady=10)

# new window on button click
btn2 = Button(master,
             text ="No", command=quit_z, font=b, activeforeground="red"
              , activebackground="pink",padx=15, pady=5, bg="floral white")
btn2.grid(row=3, column=3, padx=150, pady=10)



mainloop()
