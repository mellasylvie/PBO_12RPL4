from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Daftar Menu")
root.geometry('800x500')

tab_menu = ttk.Notebook(root)
tab_makanan = Frame(tab_menu, background='#ECE3CE')
tab_minuman = Frame(tab_menu)  

tab_menu.add(tab_makanan, text='Makanan')
tab_menu.add(tab_minuman, text='Minuman')
tab_menu.pack(expand=True, fill='both')

#konten frame makanan
frame_judul = Frame(tab_makanan, bg='#ECE3CE')
frame_judul.pack()

judul = Label(frame_judul, text='Daftar Makanan',
              font=('Arial', 14,'bold'),
              bg='#ECE3CE', pady=20)
judul.pack()

#frame daftar makanan
frame_menu = Frame(tab_makanan, bg='#ECE3CE')
frame_menu.pack()

#Gambar 1
image1 = Image.open('pecel.png')
foto1 = ImageTk.PhotoImage(image1)

gambar1 = Label(frame_menu, image=foto1)
gambar1.grid(row=0, column=0, padx=30, pady=5)

Label(frame_menu, text='Pecel Madiun',
      font=('Arial',11,'bold'),
      bg='#ECE3CE').grid(row=1, column=0)
 
#gambar 2
image2 = Image.open('mie_ayam.png')
foto2 = ImageTk.PhotoImage(image2)

gambar2 = Label(frame_menu, image=foto2)
gambar2.grid(row=0, column=1, padx=30, pady=5)

root.mainloop()