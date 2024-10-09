from tkinter import *
import pymysql
import tkinter.messagebox as msg


allBid = []


def book_issue():

    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = book_id.get()
    issueto = student.get()

    extractBid = "select book_id from add_book"

    try:
        cursor.execute(extractBid)
        conn.commit()
        for i in cursor:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from add_book where book_id = '"+bid+"'"
            cursor.execute(checkAvail)
            conn.commit()
            for i in cursor:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            msg.showinfo("Error", "Book ID not present")
    except:
        msg.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "insert into issue_book_table values ('"+bid+"','"+issueto+"')"
    show = "select * from issueTable"

    updateStatus = "update add_book set status = 'issued' where book_id = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cursor.execute(issueSql)
            conn.commit()
            cursor.execute(updateStatus)
            conn.commit()
            msg.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            msg.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        msg.showinfo(
            "Search Error", "The value entered is wrong, Try again")

    print(bid)
    print(issueto)

    allBid.clear()


def issue_book():
    global book_id, student,  conn, cursor, root

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

    # issue book to studuent
    lb2 = Label(labelFrame, text="Issue : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    student = Entry(labelFrame)
    student.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0',
                       fg='black', command=book_issue)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
