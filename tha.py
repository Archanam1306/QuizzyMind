from tkinter import*
from PIL import ImageTk,Image
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb
def terminate():
    window.destroy()
def nextpage():
    window.destroy()
    import screen3
def myfunction():
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
    Intro=Label(window,text=k,font=('Jokerman',18))
    Intro.place(x=250,y=165)
    nextb=Button(window,text="Yes I'm in!",command=nextpage)
    nextb.place(x=1200,y=685)
    backb=Button(window,text="I Quit",command=terminate)
    backb.place(x=900,y=685)
window=Tk()
window.title('User profile')
window.attributes('-fullscreen',True)
#window.config(bg=rgb_hack((153, 204, 255)))
bg=ImageTk.PhotoImage(file='quiz.png')
Label(window,image=bg).pack()
label1=Label(window,text='Enter your pseudo name:',fg='blue',font=('Jokerman',14))
label1.place(x=350,y=35)
data=StringVar()
textbox1=Entry(window,textvariable=data,font=('Arial',14))
textbox1.place(x=600,y=35)

button2=Button(window,command=myfunction,text='Enter')
button2.place(x=1100,y=30)

window.mainloop()

