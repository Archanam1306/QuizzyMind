from tkinter import *
import tkinter.ttk as ttk
import csv
import mysql.connector as mc
import pymysql
import sys
import csv

def connect_database():
    c=mc.connect(host='localhost',user='root',password='india123',database='project')
    cur=c.cursor()
    q='select user_id,username,score from details_with_score ORDER BY score ASC'
    cur.execute(q)
    rows=cur.fetchall()
    column_names = [i[0] for i in cur.description]
    fp = open('Scorecsv.csv', 'w')
    myFile = csv.writer(fp, lineterminator = '\n')
    myFile.writerow(column_names)   
    myFile.writerows(rows)
    fp.close()

        

connect_database()



root = Tk()
root.title("Leader Board")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("User ID", "Username", "Score"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('User ID', text="User ID", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Score', text="Score", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()
with open('Scorecsv.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        userid = row['user_id']
        username = row['username']
        score = row['score']
        tree.insert("", 0, values=(userid, username, score))
#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()
