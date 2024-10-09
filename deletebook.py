from tkinter import *
import pymysql
import tkinter.messagebox as msg


def delete_book():
    bid = book_id.get()

    delete_book_query = "delete from add_book where book_id ='"+bid+"'"
  
    try:
        cursor.execute(delete_book_query)
        conn.commit()

        msg.showinfo("delete book","book deleted") 
    except:
        msg.showinfo("delete book","can't fetch book id")

def deletebook():
    global book_id, conn, cursor, root

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


    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0',
                       fg='black',command=delete_book)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
