#Canvas = Menambahkan bentuk-bentuk
from tkinter import *
import tkinter as tk

root = Tk()
root.title("Canvas")
root.geometry("800x500")

c = Canvas(root,height=500, width=800,
           bg="#860A35")

#bikin bulat = create_oval
kepala = c.create_oval(200,50,600,450,
                       fill='#39A7FF')
pipi = c.create_oval(200, 120, 600, 450,
                     fill='white')
mata_kiri = c.create_oval(280,90,400,220,
                          fill="white",outline='black')
mata_kanan= c.create_oval(400,90,520,220,
                           fill="white",outline='black')
pupil_kiri = c.create_oval(320,135,360,175, fill="black")
pupil_kanan = c.create_oval(440,135,480,175, fill="black")
hidung = c.create_oval(370,220,430,280, fill="red")
garis_hidung = c.create_line(400,280,400,380, fill="black")
mulut = c.create_arc(280,250,520,400, fill="red", extent=-180)
kumis1 = c.create_line(250,220,360,250, fill='black')
kumis2 = c.create_line(250,260,360,260, fill='black')
kumis3 = c.create_line(250,310,360,270, fill='black')
kumis4 = c.create_line(440,250,560,220, fill='black')
kumis5 = c.create_line(440,260,560,260, fill='black')
kumis6 = c.create_line(440,270,560,310, fill='black')
c.pack()
root.mainloop()