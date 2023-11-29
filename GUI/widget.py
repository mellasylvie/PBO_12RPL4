from tkinter import *
from tkinter import font

root = Tk()
root.geometry('500x500')
root.title('widget tkinter')
root.configure(bg='white')

#Tulisan (Label)
teks = Label(root,
             text='Selamat Pagi!',
             font=('Arial',20,'bold'),
             fg = 'red',
             bg = 'yellow',
             width = 50,
             height= 5)
teks.pack()

#tombol (Button)
tombol = Button(root,
                text='Ini tombol',
                width=10,
                height=2,
                bg = 'blue')
tombol.pack()

#Inputan (Entry)
label_nama = Label(root, text="Nama")
label_nama.pack()

nama = Entry(root, width=20)
nama.pack()

password = Entry(root, show="*", width=20)
password.pack()

#Checkbutton
gender1 = Checkbutton(root,
                     text="Laki-Laki")
gender1.pack()
gender2 = Checkbutton(root,
                     text="Perempuan")
gender2.pack()

#Radiobutton 
kelas1 = Radiobutton(root,
                    text="XII RPL")
kelas2 = Radiobutton(root,
                    text="XII Mesin")
kelas3 = Radiobutton(root,
                    text="XII Listrik")
kelas1.pack()
kelas2.pack()
kelas3.pack()

root.mainloop()