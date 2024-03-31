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
    import lvl

def instructions():

    button1=Button(home,text='Instructions',command=instructions,bg='SteelBlue1',fg='white',
               font=('ariel',20,'bold'), height=1, width=9)
    button1.grid(row=0, column=1, padx=200, pady=(200,10))
    button2=Button(home,text='Enter',command=enter,bg='SteelBlue1',fg='white',
               font=('ariel',20,'bold'), height=1, width=4)
    button2.grid(row=1, column=1, padx=200, pady=(0,200))
    #Label(text="Welome to TYK, "+data.get()+"!",font=('Garuda',21),height=1).place(x=550,y=95)
    k="You will be allowed to attend 3 levels of quiz.            \n\
EACH WRONGLY ANSWERED QUESTION WILL DETECT YOUR SCORE BY 2(NEGATIVE MARKING).                   \n\
When you are finished,you will be prompted to submit your selection for grading                  \n\
The results of answers will be given once submitted.                  \n\
giving personal space to you, the user, of being able to maintain                \n\
\t\tA Once you click the next button to move on to next question you won't be                                              \n\
able go back to the previous question.      \n\
Make sure you attempt all the questions since all questions are compulsory \n\
periodically and making sure that you will stay poised and find your            \n\
\t\t'ALL THE BEST!  "                                                        

    Intro=Label(home,text=k,font=('Comic Sans',15))
    Intro.grid(row=3, column=1, padx=250, pady=80)

button1=Button(home,text='Instructions',command=instructions,bg='SteelBlue1',fg='white',
               font=('ariel',20,'bold'), height=1, width=9)
button1.grid(row=0, column=1, padx=200, pady=(200,10))
button2=Button(home,text='Enter',command=enter,bg='SteelBlue1',fg='white',
               font=('ariel',20,'bold'), height=1, width=4)
button2.grid(row=1, column=1, padx=200, pady=(0,200))


#k="You will be allowed to attend 3 levels of quiz.            \n\
#EACH WRONGLY ANSWERED QUESTION WILL DETECT YOUR SCORE BY 2(NEGATIVE MARKING).                   \n\
#When you are finished,you will be prompted to submit your selection for grading                  \n\
#The results of answers will be given once submitted.                            \n\
#\t\t Once you click the next button to move on to next question you won't be                                              \n\
#able go back to the previous question.      \n\
#Make sure you attempt all the questions since all questions are compulsory \n\
#periodically and making sure that you will stay poised and find your            \n\
#\t\t'ALL THE BEST!  "                                                        

#Intro=Label(home,text=k,font=('Comic Sans',15))
#Intro.grid(row=3, column=1, padx=250, pady=80)



home.mainloop()
