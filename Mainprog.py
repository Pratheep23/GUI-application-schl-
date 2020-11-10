
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import smtplib
import sqlite3
from datetime import date
import time
import random

connect = sqlite3.connect("user_data.db")
c = connect.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS userdat
            (Name text,
            DOB text,
            Sex text,
            Mobile integer,
            Email text,
            Type text,
            Balance integer,
            Password text,
            Recents text,
            AccountNumber integer)''')
connect.commit()
connect.close()

def main_window():
    global root
    root = Tk()
    root.title("Welcome")
    root.geometry('600x600')
    label = Label(root,bg="black",padx=600,pady=600)
    label.pack()
    button1 = Button(label,text="NEW USER",padx=30,pady=20,bg='blue',fg="white",command=registration_form)
    button2 = Button(label,text="EXISTING USER",padx=20,pady=20,bg="blue",fg="white",command=login)
    button1.place(x=180,y=260)
    button2.place(x=310,y=260)
    root.resizable(False, False)
    root.mainloop()

def login():

    def sign_in():
        connect = sqlite3.connect("user_data.db")
        c = connect.cursor()
        a = c.execute("SELECT * FROM userdat WHERE Email=? AND Password=?",(e_logemail.get(),e_logpass.get()))
        global user_details
        user_details=a.fetchall()
        connect.commit()
        connect.close()
        if(user_details==[]):
            messagebox.showerror("Incorrect Credentials","Email ID or Password entered is worng!")
        else:
            w_log.destroy()
            services()
    try:
        root.destroy()
    except:
        pass
    w_log = Tk()
    w_log.title("LOGIN")
    w_log.geometry("435x230")
    l_logemail = Label(w_log, text="Email ID: ", font=("Helvetica", 13))
    l_logpass = Label(w_log, text="Password: ", font=("Helvetica", 13))
    e_logemail = Entry(w_log, font=("Helvetica", 13), borderwidth=4, width=30)
    e_logpass = Entry(w_log, font=("Helvetica", 13), borderwidth=4, width=30,show="*")
    l_logemail.place(x=180, y=10)
    e_logemail.place(x=80, y=33)
    l_logpass.place(x=180, y=90)
    e_logpass.place(x=80, y=113)
    b_log = Button(w_log, text="SIGN-IN", font=("helvetica", 13), bg="blue", fg="white", width=10,command=sign_in)
    b_log.place(x=170, y=170)
    w_log.resizable(False,False)
    w_log.mainloop()

def services():

    def cancel():
            window.destroy()
            services()


    def fund_transfer():
        b_21.config(state=DISABLED)
        b_22.config(state=DISABLED)
        b_23.config(state=DISABLED)
        b_24.config(state=DISABLED)
        today = date.today()
        d = today.strftime("%b-%d-%Y")
        d1 = today.strftime("%d/%m/%Y")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        l_frmacc = Label(l_3,text="From Account: ",font=("Helvetica",20),bg="light grey")
        l_frmacc.place(x=20,y=30)
        l_toacc = Label(l_3,text="To Account No: ",font=("Helvetica",20),bg="light grey")
        l_toacc.place(x=20,y=130)
        l_amt = Label(l_3,text="Amount: ",font=("Helvetica",20),bg="light grey")
        l_amt.place(x=20,y=230)
        l_date = Label(l_3,text="Date: ",font=("Helvetica",20),bg="light grey")
        l_date.place(x=20,y=330)

        l_frmacc2 = Label(l_3,text=user_details[0][0],font=("Helvetica",20),bg="light grey")
        l_frmacc2.place(x=250,y=30)
        e_toacc = Entry(l_3,font=("Helvetica",20),width=25)
        e_toacc.place(x=250,y=130)
        e_amt = Entry(l_3,font=("Helvetica",20))
        e_amt.place(x=250,y=230)
        l_date2 = Label(l_3,text=d,font=("Helvetica",20),bg="light grey")
        l_date2.place(x=250,y=330)
        bs_cancel = Button(l_3,text="Cancel Transfer",font=("Helvetica",18),command=cancel)
        bs_cancel.place(x=640,y=450)

        def transfer():
            numy = str(e_toacc.get())
            y = 0
            for i in numy:
                if (i.isalpha()):
                    y += 1
            if(y!=0):
                messagebox.showerror("Uh..Oh!","Enter a Valid Account Number!")
            elif(e_toacc.get()==''):
                messagebox.showerror("Uh..Oh!", "Enter a Valid Account Number!")
            elif(e_amt.get()==''):
                messagebox.showerror("Uh..Oh!", "Enter a Valid Amount!")
            else:
                connect = sqlite3.connect("user_data.db")
                c = connect.cursor()
                r = c.execute("SELECT * FROM userdat WHERE AccountNumber=?", (int(e_toacc.get()),))
                rl = r.fetchall()
                connect.commit()
                connect.close()

                if(rl==[]):
                    messagebox.showerror("Transfer Failed","The account you are looking to transfer money is not found!")
                elif((user_details[0][6]-int(e_amt.get()))<0):
                    messagebox.showerror("Oops","Insufficient Balance!")
                else:
                    connect = sqlite3.connect("user_data.db")
                    c = connect.cursor()
                    c.execute("UPDATE userdat SET Balance=? WHERE Email=?",(user_details[0][6] - int(e_amt.get()), user_details[0][4]))
                    frm = user_details[0][4]
                    r = c.execute("SELECT * FROM userdat WHERE AccountNumber=?", (int(e_toacc.get()),))
                    rl = r.fetchall()
                    connect.commit()
                    connect.close()
                    to = rl[0][4]
                    connect = sqlite3.connect("user_data.db")
                    c = connect.cursor()
                    c.execute("UPDATE userdat SET Balance=? WHERE AccountNumber=?",(rl[0][6]+int(e_amt.get()),int(e_toacc.get())))
                    connect.commit()
                    connect.close()

                    connect = sqlite3.connect("user_data.db")
                    c = connect.cursor()
                    a = rl[0][8] + "{} has Transferred Rs.{} to your Account     Time={}     Date={},".format(
                        user_details[0][0], e_amt.get(), current_time, d)
                    c.execute("UPDATE userdat SET Recents=? WHERE AccountNumber=?", (a, int(e_toacc.get())))
                    connect.commit()
                    connect.close()
                    connect = sqlite3.connect("user_data.db")
                    c = connect.cursor()
                    b = user_details[0][8] + "You have Transferred Rs.{} to {}     Time={}     Date={},".format(e_amt.get(),
                                                                                                                rl[0][0],
                                                                                                                current_time,
                                                                                                                d)
                    c.execute("UPDATE userdat SET Recents=? WHERE Email=?", (b, user_details[0][4]))
                    connect.commit()
                    connect.close()

                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('projectmanagermailing@gmail.com','Management')
                        subject = 'Transfer Success Alert!'
                        body = '''Transfer to other\n\n--------Forwarded message--------\nFrom: projectmanagermailing@gmail.com \nDate:{}\nSubject: IMPS Transaction->Success\nTo:{}\n\n\nDear {},\nWe wish to inform you that your account is debited for Rs.{} on {} towards IMPS\n\nPlease find the details as below:\nBeneficiary Name:{}\nBeneficiary Account No:{}'''.format(d,frm,user_details[0][0],
                                                                                                                            e_amt.get(),d1,rl[0][0],e_toacc.get())
                        msg = f'Subject: {subject}\n\n{body}'
                        smtp.sendmail('projectmanagermailing@gmail.com', frm, msg)

                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('projectmanagermailing@gmail.com', 'Management')
                        subject = 'Credit Alert!!'
                        body = '\n--------Forwarded message--------\nFrom: projectmanagermailing@gmail.com\nDate: {}\nSubject: Credit Alert\nTo: {}\n\nDear Customer,\nWe wish to inform you that Rs.{} is credited to your account on {} on account of Funds Transfer from {}'.format(d,to,e_amt.get(),d1,user_details[0][0])
                        msg = f'Subject: {subject}\n\n{body}'
                        smtp.sendmail('projectmanagermailing@gmail.com', to, msg)

                    messagebox.showinfo("Fund Transfer", "Transfer was Successful!!")

                    window.destroy()
                    services()



        bs_proceed = Button(l_3,text="Proceed",font=("Helvetica",18),bg="red",fg="white",command=transfer)
        bs_proceed.place(x=850,y=450)

    def account_details():
        connect = sqlite3.connect("user_data.db")
        c = connect.cursor()
        new = c.execute("SELECT * FROM userdat WHERE Email=?", (user_details[0][4],))
        nl = new.fetchall()
        connect.commit()
        connect.close()
        b_21.config(state=DISABLED)
        b_22.config(state=DISABLED)
        b_23.config(state=DISABLED)
        b_24.config(state=DISABLED)
        ld_name = Label(l_3,text="Name: ",font=("Helvetica",20),bg="light grey")
        ld_dob = Label(l_3,text="Date of Birth: ",font=("Helvetica",20),bg="light grey")
        ld_accno = Label(l_3,text="Account Number: ",font=("Helvetica",20),bg="light grey")
        ld_id = Label(l_3,text="Email ID: ",font=("Helvetica",20),bg="light grey")
        ld_mob = Label(l_3,text="Mobile Number: ",font=("Helvetica",20),bg="light grey")
        ld_type = Label(l_3,text="Type of Account: ",font=("Helvetica",20),bg="light grey")
        ld_balance = Label(l_3,text="Account Balance: ",font=("Helvetica",20),bg="light grey")
        ld_name.place(x=20,y=20)
        ld_dob.place(x=20,y=75)
        ld_accno.place(x=20,y=130)
        ld_id.place(x=20,y=195)
        ld_mob.place(x=20,y=255)
        ld_type.place(x=20,y=315)
        ld_balance.place(x=20,y=375)


        ld_name2 = Label(l_3,text=nl[0][0],font=("Helvetica",20),bg="light grey")
        ld_dob2 = Label(l_3,text=nl[0][1],font=("Helvetica",20),bg="light grey")
        ld_accno2 = Label(l_3,text=nl[0][9],font=("Helvetica",20),bg="light grey")
        ld_id2 = Label(l_3,text=nl[0][4],font=("Helvetica",20),bg="light grey")
        ld_mob2 = Label(l_3,text=nl[0][3],font=("Helvetica",20),bg="light grey")
        ld_type2 = Label(l_3,text=nl[0][5],font=("Helvetica",20),bg="light grey")
        ld_balance2 = Label(l_3,text=nl[0][6],font=("Helvetica",20),bg="light grey")
        ld_name2.place(x=310,y=20)
        ld_dob2.place(x=310,y=75)
        ld_accno2.place(x=310,y=130)
        ld_id2.place(x=310,y=195)
        ld_mob2.place(x=310,y=255)
        ld_type2.place(x=310,y=315)
        ld_balance2.place(x=310,y=375)

        bd_goback  = Button(l_3,text="Go Back",font=("Helvetica",18),bg="red",fg="white",command=cancel)
        bd_goback.place(x=850,y=450)

    def logout():
        msg = messagebox.askquestion("Logout","Are you sure you want to Logout?")
        if(msg=="yes"):
            window.destroy()
            main_window()
        else:
            pass

    def recents():
        b_21.config(state=DISABLED)
        b_22.config(state=DISABLED)
        b_23.config(state=DISABLED)
        b_24.config(state=DISABLED)
        e_r = Text(l_3,height=200,width=1010)
        e_r.place(x=0,y=0)
        b_rcancel = Button(e_r,text ="Go Back",font=("Helvetica",18),bg="red",fg="white",command=cancel)
        b_rcancel.place(x=850, y=450)
        connect = sqlite3.connect("user_data.db")
        c = connect.cursor()
        a = c.execute("SELECT Recents FROM userdat WHERE Email=?",(user_details[0][4],))
        l = a.fetchall()[0][0].split(",")
        connect.commit()
        connect.close()
        for i in l:
            e_r.insert(END,str(i)+'\n')





    window = Tk()
    window.title("Services")
    window.geometry("1014x600")
    f1 = LabelFrame(window)
    f1.place(x=0,y=0)
    l_1 = Label(f1,text='Account: {}'.format(user_details[0][0]),font=('Helvetica',12),width=112,anchor=W)
    l_1.pack()
    f2 = LabelFrame(window)
    f2.place(x=0,y=27)
    b_21 = Button(f2,text="Fund Transfer",font=("Helvetica",13),width=27,pady=8,bg="light blue",fg='blue',command=fund_transfer)
    b_22 = Button(f2,text="Recent Activity",font=("Helvetica",13),width=27,pady=8,bg="light blue",fg='blue',command=recents)
    b_23 = Button(f2,text="Account Details",font=("Helvetica",13),width=27,pady=8,bg="light blue",fg='blue',command=account_details)
    b_24 = Button(f2,text="Logout",font=("Helvetica",13),width=27,pady=8,bg="light blue",fg='blue',command=logout)
    b_21.grid(row=0,column=0)
    b_22.grid(row=0,column=1)
    b_23.grid(row=0,column=2)
    b_24.grid(row=0,column=3)
    f3 = LabelFrame(window)
    f3.place(x=0,y=75)
    l_3 = Label(f3,bg="light grey",padx=503,pady=251)
    l_3.pack()
    window.resizable(False,False)
    window.mainloop()


def registration_form():

    def password_page():
       if(int(e_otp.get())==otp):
           w.destroy()
           wpass = Toplevel()
           wpass.geometry("380x210")
           wpass.title("Set Password")
           l_password = Label(wpass, text="Password: ", font=("Helvetica", 15))
           l_password.place(x=5, y=10)
           e_password = Entry(wpass, font=("Helvetica", 15), borderwidth=5, width=25, show="*")
           e_password.place(x=5, y=40)
           l_cpassword = Label(wpass, text="Confirm Password: ", font=("Helvetica", 15))
           l_cpassword.place(x=5, y=90)
           e_cpassword = Entry(wpass, font=("Helvetica", 15), borderwidth=5, width=25, show="*")
           e_cpassword.place(x=5, y=120)

           def create_data():
               if(e_password.get()==e_cpassword.get()):
                   name = e_name.get()
                   dob = cal.get()
                   s = sex.get()
                   mobile = int(e_num.get())
                   email = e_email.get()
                   toa = type.get()
                   balance = initial.get()
                   password = e_password.get()
                   wpass.destroy()
                   win.destroy()
                   accn=random.randrange(10000000,11000000)
                   connect = sqlite3.connect("user_data.db")
                   c = connect.cursor()
                   c.execute('''CREATE TABLE IF NOT EXISTS userdat
                                (Name text,
                                DOB text,
                                Sex text,
                                Mobile integer,
                                Email text,
                                Type text,
                                Balance integer,
                                Password text,
                                Recents text,
                                AccountNumber integer)''')
                   c.execute("INSERT INTO userdat VALUES(?,?,?,?,?,?,?,?,'',?)",(name,dob,s,mobile,email,toa,balance,password,accn))
                   connect.commit()
                   connect.close()
                   wins = Tk()
                   wins.withdraw()
                   messagebox.showinfo("Hurray!","Account Successfully Created!!")
                   wins.destroy()
                   login()



               else:
                   messagebox.showerror("Uh Oh..","Password Mismatch!")
                   wpass.destroy()
                   e_name.config(state=NORMAL)
                   cal.config(state=NORMAL)
                   e_num.config(state=NORMAL)
                   e_email.config(state=NORMAL)
                   r_sex1.config(state=NORMAL)
                   r_sex2.config(state=NORMAL)
                   d_type.config(state=NORMAL)
                   d_initial.config(state=NORMAL)
                   b_otp.config(state=NORMAL)
                   b_otp.config(state=NORMAL)



           b_create = Button(wpass, text="Create Account", font=("Helvetica", 13), bg="blue", fg="white",command=create_data)
           b_create.place(x=230, y=170)

           def password_cancel():
               wpass.destroy()
               win.destroy()
               main_window()

           b_cancel = Button(wpass, text="Cancel", font=("Helvetica", 13),command=password_cancel)
           b_cancel.place(x=150, y=170)
           wpass.mainloop()
       else:
           w.destroy()
           messagebox.showwarning('OTP Error', 'Incorrect OTP!')
           e_name.config(state=NORMAL)
           cal.config(state=NORMAL)
           e_num.config(state=NORMAL)
           e_email.config(state=NORMAL)
           r_sex1.config(state=NORMAL)
           r_sex2.config(state=NORMAL)
           d_type.config(state=NORMAL)
           d_initial.config(state=NORMAL)
           b_otp.config(state=NORMAL)
           b_otp.config(state=NORMAL)


    def otp_page():
        connect = sqlite3.connect("user_data.db")
        c = connect.cursor()
        a = c.execute("SELECT * FROM userdat")
        l = a.fetchall()
        count = 0
        for i in l:
            if (i[4] == e_email.get()):
                count += 1
        connect.commit()
        connect.close()
        numx=str(e_num.get())
        x=0
        for i in numx:
            if(i.isalpha()):
                x+=1
        if((e_name.get()=='')or(cal.get()=='')or(e_num.get()=='')or(e_email.get()=='')or(sex.get()=='None')or(type.get()=='None')or(initial.get()=='None')):
            messagebox.showwarning('Uh oh...','Fill in all the details!')
            b_otp.config(state=NORMAL)
        elif(count==1):
            messagebox.showerror("Email ID","Given Email ID has aldready been used!")
        elif (x!=0):
            messagebox.showerror("Mobile Number", "Invalid Number!\nEnter a valid Mobile Number")
        elif (len(e_num.get()) != 10):
            messagebox.showerror("Mobile Number", "Invalid Number!\nEnter a valid Mobile Number")
        else:
            e_name.config(state=DISABLED)
            cal.config(state=DISABLED)
            e_num.config(state=DISABLED)
            e_email.config(state=DISABLED)
            r_sex1.config(state=DISABLED)
            r_sex2.config(state=DISABLED)
            d_type.config(state=DISABLED)
            d_initial.config(state=DISABLED)
            b_otp.config(state=DISABLED)
            global otp
            otp = random.randrange(100000, 1000000)
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login('projectmanagermailing@gmail.com', 'Management')
                subject = 'OTP LOGIN'
                body = 'Use this code {} to sign-up'.format(otp)
                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail('projectmanagermailing@gmail.com', e_email.get(), msg)
            global w
            w = Toplevel()
            w.title("Enter OTP")
            w.geometry("360x140")
            l_info = Label(w, text="An OTP has been sent to your Email ID:", font=("Helvetica", 14))
            l_info.place(x=0, y=10)
            l_otp = Label(w, text="Enter OTP:", font=("Helvetica", 14))
            l_otp.place(x=0, y=60)
            global e_otp
            e_otp = Entry(w, width=20, borderwidth=3, font=("Helvetica", 14))
            e_otp.place(x=110, y=60)
            b_pass = Button(w, text="Set Password", bg="blue", fg="white", font=("Helvetica", 11),command=password_page)
            b_pass.place(x=220, y=100)
            w.mainloop()


    root.destroy()
    win = Tk()
    win.title("Registration Form")
    win.geometry("700x800")

    """ALL LABELS"""     #PLACING ALL THE LABELS IN THE WINDOW
    l_title = Label(win, text="Registration Form", font=('bold', 30))
    l_title.place(x=195, y=0)
    l_name = Label(win, text="Full Name:", font=("bold", 20))
    l_name.place(x=50, y=90)
    l_dob = Label(win, text="Date of Birth:", font=("bold", 20))
    l_dob.place(x=50, y=160)
    l_sex = Label(win, text="Gender:", font=("bold", 20))
    l_sex.place(x=50, y=240)
    l_num = Label(win, text="Mobile Number:", font=("bold", 20))
    l_num.place(x=50, y=320)
    l_email = Label(win, text="Email ID:", font=("bold", 20))
    l_email.place(x=50, y=400)
    l_type = Label(win, text="Type of Account:", font=("bold", 20))
    l_type.place(x=50, y=480)
    l_initial = Label(win, text="Initial Deposit:", font=("bold", 20))
    l_initial.place(x=50, y=560)

    """ENTRIES AND OTHER WIDGETS""" #PLACING ALL THE ENTRY WIDGETS
    global e_name
    e_name = Entry(win, width=30, font=("Helvetica", 15), borderwidth=3)
    e_name.place(x=310, y=95)
    global cal
    cal = DateEntry(win, width=28, year=2000, month=1, day=1,font=("Helvetica", 15),background='darkblue', foreground='white')
    cal.place(x=310,y=165)
    global e_num
    e_num = Entry(win, width=30, font=("Helvetica", 15), borderwidth=3)
    e_num.place(x=310, y=325)
    global e_email
    e_email = Entry(win, width=30, font=("Helvetica", 15), borderwidth=3)
    e_email.place(x=310, y=405)
    global sex
    sex = StringVar()
    sex.set(None)                  #PLACING ALL THE RADIOBUTTONS
    r_sex1 = Radiobutton(win, text="Male", variable=sex, value="Male", font=("Helvetica", 15))
    r_sex1.place(x=310, y=245)
    r_sex2 = Radiobutton(win, text="Female", variable=sex, value="Female", font=("Helvetica", 15))
    r_sex2.place(x=450, y=245)
    global type
    type = StringVar()
    type.set(None)                 #PLACING ALL THE DROPDOWN MENUS
    d_type = OptionMenu(win, type, "Savings Account")
    d_type.configure(width=30, bg="white", relief=SUNKEN, font=("Helvetica", 12))
    d_type.place(x=323, y=485)
    global initial
    initial = IntVar()
    initial.set(10000)
    d_initial = OptionMenu(win, initial, 10000, 20000, 30000)
    d_initial.configure(width=30, bg="white", relief=SUNKEN, font=(12))
    d_initial.place(x=323, y=565)

                                    #PLACING ALL THE BUTTONS
    def registration_cancel():
        win.destroy()
        main_window()

    b_cancel = Button(win, text="Cancel", padx=20, pady=7, bg="red", fg="white",command=registration_cancel)
    b_cancel.place(x=400, y=625)
    global b_otp
    b_otp = Button(win, text="Request OTP", padx=20, pady=7, bg="red", fg="white",command=otp_page)
    b_otp.place(x=500, y=625)

    win.resizable(False, False)
    win.mainloop()



main_window()
