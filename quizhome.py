from tkinter import*
from PIL import ImageTk
import tkinter.messagebox as mb

home=Tk()
home.geometry('1000x1000')

bgImage=ImageTk.PhotoImage(file='quiztime.jpg')
bgLabel=Label(home,image=bgImage)
bgLabel.place(x=0,y=0)

def enter():
    home.destroy()
    import loginnewcopy

def instructions():
    Label(text='Welome to Mangalyaa, '+data.get()+'!',font=('Jokerman',21),height=1).place(x=550,y=95)
    k='This app helps you look into your life with a New perspective            \n\
With Focus mode , we bring to you the peace-time you require                   \n\
to finish your activity with no distractions from this device, for                  \n\
a set amount of time. Me-time= "Time for Me", is the concept of                  \n\
giving personal space to you, the user, of being able to maintain                \n\
\t\tA Diary which can be opened only by you                                              \n\
This App also provides a final feature - To analyse your mood patterns,      \n\
how they change with time in the form of a graph, by asking specific inputs\n\
periodically and making sure that you will stay poised and find your            \n\
\t\t"Inner Peace" in the Long Run.                                                          \n\
\nYour Well-Being is our Priority :)'
    Intro=Label(window,text=k,font=('Comic Sans',18))
    Intro.place(x=250,y=165)
    
button1=Button(home,text='Instructions',command=instructions,
               width=15,bg='DarkOrchid2',fg='black',
               font=('ariel',16,'bold'))
button1.place(x=300,y=70)



button2=Button(home,text='Enter',command=enter,
               width=5,bg='SteelBlue1',fg='white',
               font=('ariel',16,'bold'))
button2.place(x=700,y=70)





home.mainloop()
