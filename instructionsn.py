from tkinter import*
from PIL import ImageTk
import tkinter.messagebox as mb

home=Tk()
home.geometry('1500x960')

bgImage=ImageTk.PhotoImage(file='instructions.jpeg')
bgLabel=Label(home,image=bgImage)
bgLabel.place(x=0,y=0)

def enter():
    home.destroy()
    import easy

def instructions():
    Label(text="Welome to TYK, "+data.get()+"!",font=('Garuda',21),height=1).place(x=850,y=95)
    k="You will be allowed to attend 3 levels of quiz.  \n\
EACH WRONGLY ANSWERED QUESTION WILL DETECT YOUR SCORE BY 2(NEGATIVE MARKING).    \n\
When you are finished,you will be prompted to submit your selection for grading                  \n\
The results of answers will be given once submitted.                            \n\
\t\t Once you click the next button to move on to next question you won't be                                              \n\
able go back to the previous question.      \n\
Make sure you attempt all the questions since all questions are compulsory \n\
periodically and making sure that you will stay poised and find your    \n\
\t'ALL THE BEST!  "                                                        

    Intro=Label(home,text=k,font=('Comic Sans',18))
    Intro.place(x=100,y=165)
    
button1=Button(home,text='Instructions',command=instructions,
               width=15,bg='misty rose',fg='black',
               font=('ariel',16,'bold'))
button1.place(x=500,y=70)

data=StringVar()

button2=Button(home,text='Enter',command=enter,
               width=5,bg='SteelBlue1',fg='white',
               font=('ariel',16,'bold'))
button2.place(x=300,y=70)





home.mainloop()
