from tkinter import *
from tkinter import ttk

class Siswa:
    def __init__(self):
        self.nama = ""
        self.alamat = ""

    def set_nama(self, nama):
        self.nama = nama

    def get_nama(self):
        return self.nama

    def set_alamat(self, alamat):
        self.alamat = alamat

    def get_alamat(self):
        return self.alamat

def tambah_siswa():
    nama = nama_entry.get()
    alamat = alamat_entry.get()

    siswa = Siswa()
    siswa.set_nama(nama)
    siswa.set_alamat(alamat)

    frame_data = Frame(root)
    frame_data.pack()

    label_nama = Label(frame_data, text="Nama :")
    label_nama.grid(row=0, column=0)

    data_nama = Label(frame_data, text=siswa.get_nama())
    data_nama.grid(row=0, column=1)

    label_alamat = Label(frame_data, text="Alamat :")
    label_alamat.grid(row=2, column=0)

    data_alamat = Label(frame_data, text=siswa.get_alamat())
    data_alamat.grid(row=2, column=1)

    def reset_data():
        for widget in frame_data.winfo_children():
            widget.destroy()
        frame_data.destroy()

    reset_button = Button(frame_data, text="Hapus Data", command=reset_data)
    reset_button.grid(row=3, column=0, columnspan=2, pady=5)

    separator = ttk.Separator(frame_data, orient='horizontal')
    separator.grid(row=4, column=0, columnspan=2, sticky="ew", pady=5)

root = Tk()
root.title("Input Data Siswa")
root.geometry("500x500")

# Label Judul
judul = Label(root, text="Data Diri Siswa", font=('Arial', 14, 'bold'))
judul.pack()

frame_input = Frame(root)
frame_input.pack()

# Membuat label dan input untuk nama
nama_label = Label(frame_input, text="Nama:")
nama_label.grid(row=0, column=0, padx=5, pady=5)
nama_entry = Entry(frame_input, width=50)
nama_entry.grid(row=0, column=1, padx=5, pady=5)

# Membuat label dan input untuk alamat
alamat_label = Label(frame_input, text="Alamat:")
alamat_label.grid(row=1, column=0, padx=5, pady=5)
alamat_entry = Entry(frame_input, width=50)
alamat_entry.grid(row=1, column=1, padx=5, pady=5)

# Membuat tombol "Tambah Siswa"
tambah_button = Button(frame_input, text="Tambah Siswa", command=tambah_siswa)
tambah_button.grid(row=2, column=1)

root.mainloop()