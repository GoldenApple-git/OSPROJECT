import tkinter
import sys
from functools import partial
import datetime as dt
from time import sleep
from PIL import Image, ImageTk

class Idle:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.geometry(f"{int(self.window.winfo_screenwidth())}x{int(self.window.winfo_screenheight())}")
        self.window.title("")
        background_image=ImageTk.PhotoImage(master=self.window, file=".\\images\\back.png")
        background_label = tkinter.Label(self.window, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0,height=int(self.window.winfo_screenheight()), width=int(self.window.winfo_screenwidth()))
        self.text1 = tkinter.StringVar()
        self.text2 = tkinter.StringVar()

    def key_pressed(self,event):
        self.window.destroy()

    def time(self):
        self.A.config(text=f"{dt.datetime.now():%a, %b %d %Y}",bg="#170f0e",fg="#a3a0a0",font=("Courier", 25))
        self.B.config(text=f"{dt.datetime.now():%H:%M:%S}",bg="#170f0e",fg="#a3a0a0",font=("Courier", 25))
        self.B.after(1000, self.time)

    def show(self):
        self.A=tkinter.Label(self.window, text=f"{dt.datetime.now():%a, %b %d %Y}")
        self.B=tkinter.Label(self.window, text=f"{dt.datetime.now():%H:%M:%S}")
        self.window.bind("<Key>",self.key_pressed)
        self.window.bind("<Button-1>",self.key_pressed)
        self.window.bind("<Button-2>",self.key_pressed)
        self.window.bind("<Button-3>",self.key_pressed)
        self.A.pack(anchor="nw",pady=(5),padx=(5))
        self.B.pack(anchor="nw",pady=(5, 5),padx=(5))
        self.time()
        self.window.mainloop()