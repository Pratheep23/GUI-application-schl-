from tkinter import *

win = Tk()
win.title("Registration Form")
win.geometry("700x800")

"""ALL LABELS"""
l_title = Label(win,text="Registration Form",font=('bold',30))
l_title.place(x=195,y=0)
l_name = Label(win,text="Full Name:",font=("bold",20))
l_name.place(x=50,y=90)
l_dob = Label(win,text="Date of Birth:",font=("bold",20))
l_dob.place(x=50,y=160)
l_sex = Label(win,text="Sex:",font=("bold",20))
l_sex.place(x=50,y=240)
l_num = Label(win,text="Mobile Number:",font=("bold",20))
l_num.place(x=50,y=320)
l_email = Label(win,text="Email ID:",font=("bold",20))
l_email.place(x=50,y=400)
l_type = Label(win,text="Type of Account:",font=("bold",20))
l_type.place(x=50,y=480)
l_initial = Label(win,text="Initial Deposit:",font=("bold",20))
l_initial.place(x=50,y=560)

"""ENTRIES AND OTHER WIDGETS"""
e_name = Entry(win,width=30,font=("Helvetica",15),borderwidth=3)
e_name.place(x=310,y=95)
e_dob = Entry(win,width=30,font=("Helvetica",15),borderwidth=3)
e_dob.place(x=310,y=165)
e_dob.insert(0, 'dd/mm/yyyy')
e_num = Entry(win,width=30,font=("Helvetica",15),borderwidth=3)
e_num.place(x=310,y=325)
e_email = Entry(win,width=30,font=("Helvetica",15),borderwidth=3)
e_email.place(x=310,y=405)

sex = StringVar()
sex.set(None)
r_sex1 = Radiobutton(win,text="Male",variable=sex,value="Male",font=("Helvetica",15))
r_sex1.place(x=310,y=245)
r_sex2 = Radiobutton(win,text="Female",variable=sex,value="Female",font=("Helvetica",15))
r_sex2.place(x=450,y=245)

type = StringVar()
type.set(None)
d_type = OptionMenu(win,type,"Savings Account")
d_type.configure(width=30,bg="white",relief=SUNKEN,font=("Helvetica",12))
d_type.place(x=323,y=485)

initial = IntVar()
initial.set(10000)
d_initial = OptionMenu(win,initial,10000,20000,30000)
d_initial.configure(width=30,bg="white",relief=SUNKEN,font=(12))
d_initial.place(x=323,y=565)

b_cancel = Button(win,text="Cancel",padx=20,pady=7,bg="red",fg="white")
b_cancel.place(x=400,y=625)
b_otp = Button(win,text="Request OTP",padx=20,pady=7,bg="red",fg="white")
b_otp.place(x=500,y=625)

win.resizable(False,False)
win.mainloop()

