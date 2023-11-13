from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tab Window")
root.geometry("500x500")

#untuk menambahkan tab window kita pake Notebook()
tab_menu = ttk.Notebook(root)
tab_1 = Frame(tab_menu)
tab_2 = Frame(tab_menu)

#tambah frame dengan add()
tab_menu.add(tab_1, text='Tab 1')
tab_menu.add(tab_2, text='Tab 2')

#tampilkan dengan pack()
tab_menu.pack(expand=True, fill='both')

#konten tab 1
teks = Label(tab_1, text='Ini konten tab 1')
teks.pack()

#konten tab 2
teks = Label(tab_2, text='Ini konten tab 2')
teks.pack()

root.mainloop()
