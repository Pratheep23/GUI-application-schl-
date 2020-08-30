
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)




global e_dob
    e_dob = Entry(win, width=30, font=("Helvetica", 15), borderwidth=3)
    e_dob.place(x=310, y=165)
    e_dob.insert(0, 'dd/mm/yyyy')