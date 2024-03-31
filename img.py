from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.title('Home')
win.attributes('-fullscreen',True)

# Load the image
#image=Image.open('quiz.png')



# Conver the image in TkImage
my_img=ImageTk.PhotoImage(file='quiznew.png')
Label(win,image=my_img).pack()
# Display the image with label
#label=Label(win, image=my_img)
#label.pack()
def quit_h():
    win.destroy()
def loginPage():
    win.destroy()
    import detailscopy

#buttons
b=Button(win,command=loginPage,text='Login')
b.place(x=500,y=40)

b1=Button(win,command=quit_h,text='Quit')
b1.place(x=500,y=100)


    
win.mainloop()
