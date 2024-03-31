# importing everything from tkinter  
from tkinter import *  
# importing messagebox as mb from tkinter  
from tkinter import messagebox as mb  
# importing json to utilize json file for data  
import json
import mysql.connector as mc
  
# Creating a GUI Window  
guiWindow = Tk()  
   
# setting the size of the GUI Window  
guiWindow.geometry("800x450")  
  
# setting the title of the Window  
guiWindow.title("Quiz Window")  
  
# defining the class to define the GUI components  
class myQuiz:  
    """  
    defining an initializing method which is called when  
    we will initialize a new object of the class. This method  
    will set the question count to 0. and initialize all the  
    other methods in order to display the content and make all the  
    functionalities available  
    """  
    def __init__(self):       
        # setting the question number to 0  
        self.quesNumber = 0  
  
        # assigning the question to the displayQuestion function to update later.  
        self.displayTitle()  
        self.displayQuestion()  
           
        # the opt_selected attributes holds an integer value  
        # which is used for selected option in a question.  
        self.optSelected = IntVar()  
           
        # displaying radio button for the current question and  
        # used to display options for the current question  
        self.options = self.radioButtons()  
           
        # displaying the options for the current question  
        self.displayOptions()  
           
        # displaying the button for next and exit.  
        self.buttons()  
           
        # number of questions  
        self.dataSize = len(question)  
           
        # keeping a counter of right answers  
        self.rightAnswer = 0  
  
    """  
    This method is utilized to display the result  
    It counts the number of right and wrong answers  
    and then display them at the end as a message box  
    """      
    def displayResult(self):  
        # calculating the wrong count  
        wrongCount = self.dataSize - self.rightAnswer  
        rightAnswer = f"Correct: {self.rightAnswer}"  
        wrongAnswer = f"Wrong: {wrongCount}"  
        
        #score with negative marking
        positive_score = int(self.rightAnswer*5)#5 marks awarded for right answer
        negative_Score = int(wrongCount*2)#2 marks deducted for wrong answer

        # calculating the percentage of right answers
        the_score = int(positive_score - negative_Score)
        
        total_score = int(self.dataSize*5)

        #database connection
        c=mc.connect(host='localhost',user='root',password='india123',database='project')
        cur=c.cursor()
        a='select MAX(user_id) from details_with_score'
        cur.execute(a)
        res=cur.fetchone()
        max_id=res[0]
        q="update details_with_score SET score=%s WHERE user_id=%s"
        val=(the_score,max_id)
        cur.execute(q,val)
        c.commit()
        c.close()
        
        the_perc = int(the_score/total_score*100)
        the_result = f"Score: {the_score}/{total_score} \nPercentage: {the_perc}%"  
        # showing a message box to display the result  
        mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")  
        guiWindow.destroy()
        import congrats
    """  
    This method checks the Answer after we click on Next.  
    """  
    def checkAnswer(self, quesNumber):  
        # checking for if the selected option is right  
        if self.optSelected.get() == answer[quesNumber]:  
            # if the option is right it return true  
            return True  
  
    """  
    This method is utilized to check the answer of the  
    current question by calling the checkAnswer and quesNumber.  
    if the question is right it increments the count by 1  
    and then increase the question number by 1. If it is last  
    question then it calls displayResult to show the message box.  
    else shows next question.  
    """  
    def nextButton(self):  
        # Checking whether the answer is correct  
        if self.checkAnswer(self.quesNumber):  
            # if the answer is correct it increments the correct by 1  
            self.rightAnswer += 1  
           
        # Moving to next Question by incrementing the quesNumber counter  
        self.quesNumber += 1  
           
        # checking whether the quesNumber size is equal to the data size  
        if self.quesNumber == self.dataSize:   
            # if it is correct then it displays the score  
            self.displayResult()  
              
            # destroying the GUI  
            #guiWindow.destroy()  
        else:  
            # showing the next question  
            self.displayQuestion()  
            self.displayOptions()  
  
    """  
    This method displays the two buttons on the screen.  
    The first button is the next_button which moves to next question  
    It has properties like what text it shows the functionality,  
    size, color, and property of text displayed on button. Then it  
    mentions where to place the button on the screen. The second  
    button is the exit button which we will use to close the GUI without  
    completing the quiz.  
    """  
    def buttons(self):  
          
        # The first button is the Next button  
        # to move to the next Question  
        next_button = Button(  
            guiWindow,  
            text = "Next",  
            command = self.nextButton,  
            width = 10,  
            bg = "salmon",  
            fg = "white",  
            font = ("ariel", 16, "bold")  
            )  
           
        # placing the button on the screen  
        next_button.place(x = 350, y = 380)  
           
        # The second button is the quit button  
        # which is used to Quit the GUI  
        quit_button = Button(  
            guiWindow,  
            text = "Quit",  
            command = guiWindow.destroy,  
            width = 5,  
            bg = "gold",  
            fg = "white",  
            font = ("ariel", 16, " bold")  
            )  
           
        # placing the Quit button on the screen  
        quit_button.place(x = 700, y = 50)  
  
    """  
    This method deselects the radio button on the screen.  
    Then it is used to show the options available for  
    the current question which we get through the  
    question number and Updates each of the options for  
    the current question of the radio button.     
    """  
    def displayOptions(self):  
        val = 0  
        # deselecting the options  
        self.optSelected.set(0)  
        # looping over the options to be displayed  
        # for the text of the radio buttons.  
        for opt in opts[self.quesNumber]:  
            self.options[val]['text'] = opt  
            val += 1  
  
    """  
    This method shows the current Question on the screen  
    """  
    def displayQuestion(self):  
           
        # setting the Question properties  
        quesNumber = Label(  
            guiWindow,  
            text = question[self.quesNumber],  
            width = 60,  
            font = ('ariel', 16, 'bold'),  
            anchor = 'w'  
            )  
           
        # placing the option on the screen  
        quesNumber.place(x = 70, y = 100)  
      
    """  
    This method is used to Display Title  
    """  
    def displayTitle(self):           
        # The title to be shown  
        myTitle = Label(  
            guiWindow,  
            text = "QUIZ",  
            width = 50,  
            bg = "OliveDrab1",  
            fg = "black",  
            font = ("ariel", 20, "bold")  
            )  
          
        # placing the title  
        myTitle.place(x = 0, y = 2)  
   
    """  
    This method shows the radio buttons to select the Question  
    on the screen at the specified position. It also returns a  
    list of radio button which are later used to add the options to  
    them.      
    """  
    def radioButtons(self):  
           
        # initializing the list with an empty list of options  
        qList = []  
           
        # position of the first option  
        y_pos = 150  
           
        # adding the options to the list  
        while len(qList) < 4:  
               
            # setting the radio button properties  
            radio_button = Radiobutton(  
                guiWindow,  
                text = " ",  
                variable = self.optSelected,  
                value = len(qList) + 1,  
                font = ("ariel", 14)  
                )  
              
            # adding the button to the list  
            qList.append(radio_button)  
               
            # placing the button  
            radio_button.place(x = 100, y = y_pos)  
               
            # incrementing the y-axis position by 40  
            y_pos += 40  
           
        # returning the radio buttons  
        return qList  
  
# getting the data from the json file  
with open('data.json') as json_file:  
    data = json.load(json_file)  
   
# setting the question, options, and answer  
question = (data['question'])  
opts = (data['choices'])  
answer = (data[ 'ans'])  
   
# creating an object of the myQuiz Class.  
quiz = myQuiz()  
  
# using the mainloop() function  
guiWindow.mainloop()  
