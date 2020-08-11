
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

def main_window():
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
    button1 = Button(label,text="NEW USER",padx=30,pady=20,bg='blue',fg="white")
    button2 = Button(label,text="EXISTING USER",padx=20,pady=20,bg="blue",fg="white")
    button1.place(x=180,y=260)
    button2.place(x=310,y=260)
    root.resizable(False, False)
    root.mainloop()

main_window()