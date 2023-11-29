from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Halaman Login")
root.geometry('500x300')

judul = Label(root,
              text='Login',
              font=('Arial', 18,'bold')
              )
judul.pack()

username = Label(root,
                 text='Username')
username.pack()

input_user = Entry(root,width=20)
input_user.pack()

password = Label(root,
                 text='Password')
password.pack()

input_pass = Entry(root,width=20,show="*")
input_pass.pack()

def pesan() :
    tkinter.messagebox.showinfo("info", "Login berhasil")

tombol = Button(root, 
                text="Log in",
                width=7,
                command=pesan)                                      
tombol.pack()

root.mainloop()