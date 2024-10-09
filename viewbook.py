from tkinter import *
import tkinter.messagebox as msg
import pymysql

conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        database="library_db"
    )
cursor = conn.cursor()
def viewbook():
    global book_id, book_title, book_author, book_status, conn, cursor, root

    root = Tk()
    root.title("Libray Management")
    root.geometry("600x600")

    root.configure(bg="blue")

    

    frame = Frame(root, borderwidth=6, bg="yellow")
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label = Label(frame, text="View Book List", bg="black",
                  fg="white", font="lucida 19 bold")
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    label = Label(labelFrame, text="Bid------Title------Author------status",
                  bg="white", font="lucida 12 bold")
    label.place(relx=0.1, rely=0.2, relheight=0.14, relwidth=0.8)

    getbooks = "select * from add_book"

    try:
        y =0.5
        cursor.execute(getbooks)
        conn.commit()
        for i in cursor:
            label = Label(labelFrame, text=(i[0]+"------"+i[1]+"------"+i[2] +
                  "------"+i[3]), bg='black', fg='white',font="lucida 12 bold")
            label.place(relx=0.1, rely=y, relheight=0.14, relwidth=0.8)
            y = y+0.1
    except:
        msg.showinfo("View Book","Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.35, rely=0.9, relwidth=0.18, relheight=0.08)