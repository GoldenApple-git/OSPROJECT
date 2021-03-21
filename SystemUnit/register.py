import tkinter
from functools import partial
from cryptmdp import *

class Reg:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(bg="#131416")
        self.window.attributes('-fullscreen', True)
        self.window.geometry(f"{int(self.window.winfo_screenwidth())}x{int(self.window.winfo_screenheight())}")
        self.window.title("")
        self.window.grid_columnconfigure((0), weight=1)
        self.text1 = tkinter.StringVar()
        self.text2 = tkinter.StringVar()

    def save(self,passw,user):
        modifpassw = brainfuck_print([letter_to_brainfuck(i) for i in list(passw.get())])
        open("./settingsdata.db", "a", newline="").write(f"#\naccount,{user.get()},{modifpassw}")
        self.window.destroy()

    def show(self):
        tkinter.Label(self.window, text = "Register :",bg="#131416",fg="#a3a0a0",font=("Courier", 27)).grid(pady=(int(self.window.winfo_screenheight())/5, 0))
        tkinter.Label(self.window, text = "Username",bg="#131416",fg="#a3a0a0",font=("Courier", 17)).grid(pady=(int(self.window.winfo_screenheight())/6, 1))
        tkinter.Entry(self.window, textvariable=self.text1).grid(pady=(1, 5))
        tkinter.Label(self.window, text = "Password",bg="#131416",fg="#a3a0a0",font=("Courier", 17)).grid(pady=(1, 1))
        tkinter.Entry(self.window, textvariable=self.text2).grid(pady=(1, 1))
        save = partial(self.save, self.text2, self.text1)
        tkinter.Button(self.window, text = "Done",width=15,bg="#3b3d40",fg="#a3a0a0", command = save).grid(pady=(5))
        self.window.mainloop()