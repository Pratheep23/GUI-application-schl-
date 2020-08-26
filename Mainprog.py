
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random

def main_window():
    global root
    root = Tk()
    root.title("Welcome")
    root.geometry('600x600')

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo

    image = Image.open(r'Images/images3.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)
    button1 = Button(label,text="NEW USER",padx=30,pady=20,bg='blue',fg="white",command=registration_form)
    button2 = Button(label,text="EXISTING USER",padx=20,pady=20,bg="blue",fg="white")
    button1.place(x=180,y=260)
    button2.place(x=310,y=260)
    root.resizable(False, False)
    root.mainloop()

def registration_form():

    def otp_page():
        if((e_name.get()=='')or(e_dob.get()=='')or(e_num.get()=='')or(e_email.get()=='')or(sex.get()=='None')or(type.get()=='None')or(initial.get()=='None')):
            msg_box = messagebox.showwarning('Uh oh...','Fill in all the details!')
            b_otp.config(state=NORMAL)
        else:
            b_otp.config(state=DISABLED)
            w = Toplevel()
            w.title("Enter OTP")
            w.geometry("360x140")
            l_info = Label(w, text="An OTP has been sent to your Email ID:", font=("Helvetica", 14))
            l_info.place(x=0, y=10)
            l_otp = Label(w, text="Enter OTP:", font=("Helvetica", 14))
            l_otp.place(x=0, y=60)
            e_otp = Entry(w, width=20, borderwidth=3, font=("Helvetica", 14))
            e_otp.place(x=110, y=60)
            b_pass = Button(w, text="Set Password", bg="blue", fg="white", font=("Helvetica", 11))
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
    l_sex = Label(win, text="Sex:", font=("bold", 20))
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
    global e_dob
    e_dob = Entry(win, width=30, font=("Helvetica", 15), borderwidth=3)
    e_dob.place(x=310, y=165)
    e_dob.insert(0, 'dd/mm/yyyy')
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
    b_cancel = Button(win, text="Cancel", padx=20, pady=7, bg="red", fg="white")
    b_cancel.place(x=400, y=625)
    global b_otp
    b_otp = Button(win, text="Request OTP", padx=20, pady=7, bg="red", fg="white",command=otp_page)
    b_otp.place(x=500, y=625)

    win.resizable(False, False)
    win.mainloop()


main_window()

