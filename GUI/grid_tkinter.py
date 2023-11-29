from tkinter import *

root = Tk()
root.title('Grid Tkinter')
root.geometry('500x300')

nama = Label(root,
             text='Nama :').grid(row=0, column=0, padx=(20,5))

field_nama = Entry(root,
                   width=20).grid(row=0, column=1, padx=(5,10))

alamat = Label(root,
               text='Alamat :').grid(row=0, column=2, padx=(5,5))

field_alamat = Entry(root, width=20).grid(row=0, column=3)
root.mainloop()