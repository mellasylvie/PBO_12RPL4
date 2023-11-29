from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Halaman Login')
root.geometry('500x500')

judul = Label(root, 
              text="Login",
              font=('Arial', 14),
              pady=15)
judul.pack()

image = Image.open("profile.png")
logo = ImageTk.PhotoImage(image)

gambar = Label(root, image=logo)
gambar.pack()

frame1 = Frame(root, pady=20)
frame1.pack()

username = Label(frame1, 
                 text='Username :',
                 font=('Arial',10)).grid(row=0, column=0)

field_user = Entry(frame1, width=30).grid(row=0, column=1)

password = Label(frame1, 
                 text='Password :',
                 font=('Arial',10)).grid(row=1, column=0)

field_user = Entry(frame1, width=30, show="*").grid(row=1, column=1)

submit = Button(frame1, width=10, text="Login").grid(row=2, column=1)

root.mainloop()