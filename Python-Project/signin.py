from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

# Functionality
def clear():
    txtName.delete(0,END)
    txtPassword.delete(0,END)

def forgot_page():
    def change_password():
        if user_entry.get() == '' or newpass_entry.get() == '' or conf_pass_entry == '':
            messagebox.showerror('Error','All Fields Are Required', parent=window)
        elif newpass_entry.get() != conf_pass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matched', parent=window)
        else:
            conn = mysql.connector.connect(host='localhost',
                                           username='Thanikasalam',
                                           port=3307,
                                           password='thani@$6050T',
                                           database='userdata')
            mycursor = conn.cursor()
            query = 'select * from data where username = %s'
            mycursor.execute(query, (user_entry.get(),))
            row = mycursor.fetchone()
            if row ==None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password =%s where username = %s'
                mycursor.execute(query, (newpass_entry.get(),user_entry.get()))
            conn.commit()
            conn.close()

            messagebox.showinfo('Successful', 'Password is reset, Please login with new password', parent=window)
            window.destroy()

    window = Toplevel()
    window.resizable(False,False)
    window.title('Change Password')

    varimage = ImageTk.PhotoImage(file='background.jpg')
    backgroud_lbl = Label(window, image=varimage)
    backgroud_lbl.grid()

    headlbl = Label(window, text='RESET PASSWORD', font=('arial', 20, 'bold'),
                    bg='white', fg='magenta2')
    headlbl.place(x=480, y=60)

    userlbl = Label(window, text='Username', font=('arial', 12, 'bold'),fg='orchid1', bg='white')
    userlbl.place(x=470, y=130)

    user_entry = Entry(window, width=25, font=('arial', 11, 'bold'), fg='magenta2', bd=0)
    user_entry.place(x=470, y=160)

    frame3 = Frame(window, width=250, height=2, bg='orchid1')
    frame3.place(x=470, y=180)

    new_passlbl = Label(window, text='New Password', font=('arial', 12, 'bold'), fg='orchid1', bg='white')
    new_passlbl.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0,
                       fg='magenta2')
    newpass_entry.place(x=470, y=240)

    frame4 = Frame(window, width=250, height=2, bg='orchid1')
    frame4.place(x=470, y=260)

    conf_pass_lbl = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white',
                          fg='orchid1')
    conf_pass_lbl.place(x=470, y=290)

    conf_pass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0,
                            fg='magenta2', bg='white')
    conf_pass_entry.place(x=470, y=320)

    frame5 = Frame(window, width=250, height=2, bg='orchid1')
    frame5.place(x=470, y=340)

    submit_btn = Button(window, text='Submit', font=('Open Sans', 16, 'bold'),
                        fg='white', activeforeground='white', bg='magenta2',
                        activebackground='magenta2', cursor='hand2', width=19, bd=0,
                        command=change_password)
    submit_btn.place(x=474, y=390)

    window.mainloop()


def login_user():
    if txtName.get() == '' or txtPassword.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            conn = mysql.connector.connect(host='localhost',
                                       username='Thanikasalam',
                                       port=3307,
                                       password='thani@$6050T',
                                       database='mysql')
            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username = %s and password = %s'
        mycursor.execute(query,(txtName.get(), txtPassword.get()))
        row = mycursor.fetchone()
        if row ==None:
            messagebox.showerror('Error','Inavalid username or password')
        else:
            messagebox.showinfo('welcome','Login is successful')
            clear()

def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.config(file='closeye.png')
    txtPassword.config(show='*')
    btneye.config(command=show)


def show():
    openeye.config(file='openeye.png')
    txtPassword.config(show='')
    btneye.config(command=hide)



def name_enter(variable):
    if txtName.get() == 'Username':
        txtName.delete(0,END)


def password_enter(ano_variable):
    if txtPassword.get() == 'Password':
        txtPassword.delete(0,END)



# GUI Part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(False,False)
login_window.title('Login')

bgImage = ImageTk.PhotoImage(file='bg.jpg')


bglabel = Label(login_window, image=bgImage)
bglabel.place(x=0, y=0)


lblHeading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahel UI Light',23, 'bold')
                    ,bg='white', fg='firebrick1')
lblHeading.place(x=605, y=120)

txtName = Entry(login_window, width=25, font=('Microsoft Yahel UI Light', 11,'bold')
                    ,bd=0, fg='firebrick1')
txtName.place(x=580, y=200)
txtName.insert(0,'Username')

txtName.bind('<FocusIn>', name_enter)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

txtPassword = Entry(login_window, width=25, font=('Microsoft Yahel UI Light', 11, 'bold'),
                    bd=0, fg='firebrick1')
txtPassword.place(x=580, y=260)
txtPassword.insert(0,'Password')

txtPassword.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
btneye = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white'
                ,cursor='hand2', command=hide)
btneye.place(x=800, y=255)

btnforgot= Button(login_window, text='Forgot Password?', bg='white', bd=0,
                   fg='firebrick1', activebackground='white', cursor='hand2',
                   font=('Microsoft yahel UI Light',9, 'bold'), activeforeground='firebrick1', command=forgot_page)
btnforgot.place(x=715, y=295)

btnlogin = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),fg='white',
                  bg='firebrick1', activeforeground='white', activebackground='firebrick1',
                  bd=0, cursor='hand2', width=20, command=login_user)
btnlogin.place(x=569, y=340)

lblor = Label(login_window, text='---------------OR---------------', font=('Open Sans', 16, 'bold'),
              fg='firebrick1', bg='white')
lblor.place(x=577, y=390)


google_logo = PhotoImage(file='goole6.png')
btngoogle = Button(login_window, image=google_logo, bg='white', bd=0, activebackground='white',
                   cursor='hand2')
btngoogle.place(x=576, y=430)

lblsignup = Label(login_window, text="Don't have an account?", font=('Open Sans', 9, 'bold'),
                  fg='firebrick1', bg='white')
lblsignup.place(x=580,y=500)

btncre_acc = Button(login_window, text='Create new one', bd=0,bg='white', activebackground='white',
                    cursor='hand2', font=('Open Sans', 9, 'bold underline'), activeforeground='blue',
                    fg='blue', command=signup_page)
btncre_acc.place(x=720, y=500)

login_window.mainloop()
