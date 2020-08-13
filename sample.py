from tkinter import *

w = Tk()
w.title("Enter OTP")
w.geometry("360x140")
l_info = Label(w,text="An OTP has been sent to your Email ID:",font=("Helvetica",14))
l_info.place(x=0,y=10)
l_otp = Label(w,text="Enter OTP:",font=("Helvetica",14))
l_otp.place(x=0,y=60)
e_otp = Entry(w,width=20,borderwidth=3,font=("Helvetica",14))
e_otp.place(x=110,y=60)
b_pass = Button(w,text="Set Password",bg="blue",fg="white",font=("Helvetica",11))
b_pass.place(x=220,y=100)
w.mainloop()
