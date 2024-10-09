from tkinter import *
import tkinter.messagebox as msg
import pymysql


def bookdetails():
    bid = book_id.get()
    btitle = book_title.get()
    bauthor = book_author.get()
    bstatus = book_status.get()

    print(bid, "---", btitle, "---", bauthor, "---", bstatus)

    insert_book_details = "insert into add_book()values('"+bid+"','"+btitle + \
        "','"+bauthor+"','"+bstatus+"')"
    try:
        cursor.execute(insert_book_details)
        conn.commit()

        msg.showinfo("Add Book", "Book added successfully")
    except:
        msg.showinfo("Add Book", "insert failed")

    root.destroy()


def addbook():

    global book_id, book_title, book_author, book_status, conn, cursor, root

    root = Tk()
    root.title("Libray Management")
    root.geometry("600x600")

    root.configure(bg="blue")
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        database="library_db"
    )
    cursor = conn.cursor()

    frame = Frame(root, borderwidth=6, bg="yellow")
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label = Label(frame, text="Add Book", bg="black",
                  fg="white", font="lucida 19 bold")
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    book_id = Entry(labelFrame)
    book_id.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    book_title = Entry(labelFrame)
    book_title.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    book_author = Entry(labelFrame)
    book_author.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ",
                bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    book_status = Entry(labelFrame)
    book_status.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0',
                       fg='black', command=bookdetails)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
