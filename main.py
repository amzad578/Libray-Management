from tkinter import *
import pymysql
import tkinter.messagebox as msg

from addbook import *
from deletebook import *
from viewbook import *
from returnbook import *
from issuebook import *

root = Tk()
root.title("Libray Management")
root.geometry("600x600")

root.configure(bg="blue")


try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        database="library_db"
    )
    cursor = conn.cursor()
except:
    msg.showinfo("database connection", "Could not connect to database")


frame = Frame(root, borderwidth=4, bg="yellow")
frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

label = Label(frame, text="Library", bg="black",
              fg="white", font="lucida 19 bold")
label.place(relx=0, rely=0, relwidth=1, relheight=1)

b1 = Button(root, text="Add Book", bg="black", fg="white",
            font="lucida 19 bold", command=addbook)
b1.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)


b2 = Button(root, text="issue Book", bg="black",
            fg="white", font="lucida 19 bold", command=issue_book)
b2.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.1)

b3 = Button(root, text="Delete Book", bg="black",
            fg="white", font="lucida 19 bold", command=deletebook)
b3.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.1)

b4 = Button(root, text="Return Book", bg="black",
            fg="white", font="lucida 19 bold" ,command=returnbook)
b4.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)

b5 = Button(root, text="View Book", bg="black",
            fg="white", font="lucida 19 bold", command=viewbook)
b5.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

root.mainloop()
