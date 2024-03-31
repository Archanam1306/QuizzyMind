from tkinter import*
from PIL import ImageTk


home=Tk()
home.geometry('1000x1000')

bgImage=ImageTk.PhotoImage(file='quiztime.jpg')
bgLabel=Label(home,image=bgImage)
bgLabel.place(x=0,y=0)

def enter():
    home.destroy()
    import loginnewcopy


button2=Button(home,text='Enter',command=enter,
               width=5,bg='DarkOrchid2',fg='white',
               font=('ariel',16,'bold'))
button2.place(x=700,y=70)





home.mainloop()
