import tkinter
from functools import partial
from cryptmdp import *
from Commands.console import Consola
from StartSession import Launch

class Login:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(bg="#131416")
        self.window.attributes('-fullscreen', True)
        self.window.geometry(f"{int(self.window.winfo_screenwidth())}x{int(self.window.winfo_screenheight())}")
        self.window.title("")
        self.window.grid_columnconfigure((0), weight=1)
        self.rawdata = open("./settingsdata.db", "r", newline="").read().split("#")
        self.text1 = tkinter.StringVar()
        self.text2 = tkinter.StringVar()

    def login(self,passw,user,event=None):
        for lines in self.rawdata:
            if "account" in tuple(lines.split(","))[0]:
                if user.get() == tuple(lines.split(","))[1]:
                    if passw.get() == start(tuple(lines.split(","))[2]):
                        self.window.destroy()
                        L = Launch(user.get())
                        L.start()

    def show(self):
        tkinter.Label(self.window, text = "Login :",bg="#131416",fg="#a3a0a0",font=("Courier", 27)).grid(pady=(int(self.window.winfo_screenheight())/5, 0))
        tkinter.Label(self.window, text = "Username",bg="#131416",fg="#a3a0a0",font=("Courier", 17)).grid(pady=(int(self.window.winfo_screenheight())/6, 1))
        tkinter.Entry(self.window, textvariable=self.text1).grid(pady=(1, 5))
        tkinter.Label(self.window, text = "Password",bg="#131416",fg="#a3a0a0",font=("Courier", 17)).grid(pady=(1, 1))
        tkinter.Entry(self.window, textvariable=self.text2).grid(pady=(1, 1))
        login = partial(self.login, self.text2, self.text1)
        tkinter.Button(self.window, text = "Done",width=15,bg="#3b3d40",fg="#a3a0a0", command = login).grid(pady=(5))
        self.window.bind('<Return>', login)
        self.window.mainloop()