from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector


def clear():
    txtEmail.delete(0,END)
    txtUsername.delete(0,END)
    txtPassword.delete(0,END)
    txtConfirm_passw.delete(0,END)
    check.set(0)


def connect_database():
    if txtEmail.get() == '' or txtUsername.get() == '' or txtPassword.get() == '' or txtConfirm_passw.get() == '':
        messagebox.showerror('Error','All Fields Are Required!')
    elif txtPassword.get() != txtConfirm_passw.get():
        messagebox.showerror('Error','Password Mismacth')
    elif check.get() ==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        try:
            conn = mysql.connector.connect(host='localhost',
                                           username='Thanikasalam',
                                           port=3307,
                                           password='thani@$6050T',
                                           database='mysql')

            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'CREATE DATABASE userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = ("CREATE TABLE data (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(55), username VARCHAR(55)),"
                     " password VARCHAR(20)")
            mycursor.execute(query)



        except:
            mycursor.execute('use userdata')


        query = 'select * from data where username = %s'
        mycursor.execute(query,(txtUsername.get(),))
        row = mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','username Already Exists')
        else:
            email = txtEmail.get()
            username = txtUsername.get()
            password = txtPassword.get()
            query = "INSERT INTO data(email, username, password) values( %s, %s, %s)"
            mycursor.execute(query, (email, username, password))
            # commit changes and close connection...
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Registration is successfully')
            clear()
            signup_window.destroy()
            import signin

def login_page():
    signup_window.destroy()
    import signin


signup_window = Tk()
signup_window.resizable(False,False)
signup_window.title('Signup Page')
background = ImageTk.PhotoImage(file='bg.jpg')

lblbg = Label(signup_window, image=background)
lblbg.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=554, y=100)

lblhead = Label(frame, text='CREATE AN ACCOUNT', font=('MICROSOFT Yahel UI Light', 18, 'bold'),
            fg='firebrick1', bg='white')
lblhead.grid(row=0, column=0, padx=10, pady=10)

lblEmail = Label(frame, text='Email', font=('Microsoft Yahel UI Light', 10, 'bold'),
                 bg='white', fg='firebrick1')
lblEmail.grid(row=1, column=0, sticky='w', padx=25, pady=(10,0))

txtEmail = Entry(frame,width=35, font=('Microsoft Yahel UI Light', 10, 'bold'),
                fg='white', bg='firebrick1', bd=1)
txtEmail.grid(row=2, column=0, sticky='w', padx=25)

lblUsername = Label(frame, text='Username', font=('Microsoft Yahel UI Light', 10, 'bold')
                   , bg='white', fg='firebrick1')
lblUsername.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))

txtUsername = Entry(frame,width=35, font=('Microsoft Yahel UI light', 10, 'bold'),
                    fg='white', bg='firebrick1')
txtUsername.grid(row=4, column=0, sticky='w', padx=25)

lblpassword = Label(frame, text='password', font=('Microsoft Yahel UI Light', 10, 'bold'),
                    bg='white', fg='firebrick1')
lblpassword.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))

txtPassword = Entry(frame,width=35, font=('Microsoft yahel UI Light', 10, 'bold'),
                    fg='white', bg='firebrick1')
txtPassword.grid(row=6, column=0, sticky='w', padx=25)

lblConfirm_passw = Label(frame, text='Confirm Password', font=('Microsoft Yahel UI Light', 10, 'bold'),
                         bg='white', fg='firebrick1')
lblConfirm_passw.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))

txtConfirm_passw = Entry(frame,width=35, font=('Microsoft Yahel UI Light', 10, 'bold'),
                         fg='white', bg='firebrick1')
txtConfirm_passw.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
TermsandCond_btncheck = Checkbutton(frame, text='I agree to the Terms and Conditions',font=('Open Sans',
                                    10, 'bold'),bg='white', fg='firebrick1', activeforeground='firebrick1',
                                     activebackground='white', cursor='hand2', variable=check)
TermsandCond_btncheck.grid(row=9, column=0, sticky='w', pady=10, padx=15)

btnsignup = Button(frame, text='Signup', font=('Open Sans', 16, 'bold'),  bd=0, fg='white', bg='firebrick1'
                 , activebackground='firebrick1', activeforeground='white', width=18, cursor='hand2',
                   command=connect_database)
btnsignup.grid(row=10, column=0, pady=10)

alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans', 9, 'bold'), bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w', pady=10, padx=25)

btnlogin = Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'),
                  bg='white', fg='blue', cursor='hand2', activebackground='white',
                  activeforeground='blue', bd=0, command=login_page)
btnlogin.place(x=170,y=375)

signup_window.mainloop()
