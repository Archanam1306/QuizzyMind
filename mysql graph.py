# Connecting to mysql database
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
 
 
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="password",
                               database="student_info")
mycursor = mydb.cursor()
 
# Fecthing Data From mysql to my python progame
mycursor.execute("select Name, Marks from student_marks")
result = mycursor.fetchall
 
Names = []
Marks = []
 
for i in mycursor:
    Names.append(i[0])
    Marks.append(i[1])
     
print("Name of Students = ", Names)
print("Marks of Students = ", Marks)
 
 
# Visulizing Data using Matplotlib
plt.bar(Names, Marks)
plt.ylim(0, 5)
plt.xlabel("Name of Students")
plt.ylabel("Marks of Students")
plt.title("Student's Information")
plt.show()
