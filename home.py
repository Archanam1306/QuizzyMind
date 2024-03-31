from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

f=("Arial",25)
b=("Arial",15)

def loginPage():
    first.destroy()
    import detailscopy

#Creating tkinter window
first=Tk()

#Setting width and height of tkinter window
first.geometry("1050x800")

#Setting background color of tkinter window
first['bg']='grey'

#Setting title of tkinter window
first.title('Home Page')

#Function to display pop-up window
def msg():
    messagebox.showinfo("Redirecting to new page","Button clicked")

def quit():
    first.destroy()




#Label text for welcome
welcome = Label(first, text = "Welcome to the QUIZ", font=f, bg='grey')
welcome.grid(row=0, column=3, padx=150, pady=10)
#slider
count=0
sliderwords=''
def slider():
    global count,sliderwords
    text='read'
    if(count>=len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    label.configure(text=sliderwords)
    label.after(250,slider)
label=Label(first,font=('Comic Sans MS',18),fg='black',bg='grey')
label.pack()

slider()



#Create image using PhotoImage and display
img = ImageTk.PhotoImage(Image.open("quiz.jpeg"))
panel = Label(first, image = img)
panel.grid(row=1,column=3)

#Buttons definition for navigation
b1=Button(first,text="Login to Start Quiz",font=('Comic Sans MS',18),fg='black',bg='grey')
bt2=Button(first, text="Quit", font=('Comic Sans MS',18),fg='black',bg='grey'), command=quit, activeforeground="green", activebackground="red")
#b1.grid(row=2, column=3, padx=150, pady=10)
#b2.grid(row=3, column=3, padx=150, pady=10)'''

#Displaying instructions using labels
inst = Label(first, text = "Instructions" ,font=('Comic Sans MS',18),fg='black',bg='grey')
instruction3 = Label(first, text = "Each question will be for 5 marks.",font=('Comic Sans MS',18),fg='black',bg='grey')
instruction4 = Label(first, text = "The difficulty level will increase depending upon your score." ,font=('Comic Sans MS',18),fg='black',bg='grey')
instruction5 = Label(first, text = "Each wrongly answered question will detect your score by 2 - NEGATIVE MARKING." ,font=('Comic Sans MS',18),fg='black',bg='grey')



#Calling first mainloop to open rkinter window
first.mainloop()
