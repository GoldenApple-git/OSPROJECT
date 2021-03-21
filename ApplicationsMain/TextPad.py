from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from tkinter.filedialog import *
import os
from tkinter.font import Font

class TextNote:
    def __init__(self,file):
        self.file = file
        self.root = Tk()
        self.root.configure(bg='#bbc0c7')
        self.root.attributes('-fullscreen', True)
        self.TextArea = Text(self.root)
        self.MenuBar = Menu(self.root)
        self.FileMenu = Menu(self.MenuBar, tearoff=0)
        self.root.title(os.path.basename(self.file))
        self.MenuBar.configure(bg="#0c0c0d")
        self.TextArea.delete(1.0,END)
        self.TextArea.configure(bg='#131416',fg="#b3b3b5")
        self.ScrollBar = Scrollbar(self.TextArea)
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        left = (self.screenWidth / 2)
        top = (self.screenHeight / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.screenWidth, self.screenHeight, left, top))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.TextArea.grid(sticky = N + E + S + W)
        self.FileMenu.add_command(label="Save",command=self.saveFile)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit",command=self.quitApplication)
        self.MenuBar.add_cascade(label="File", menu=self.FileMenu)
        self.root.config(menu=self.MenuBar)
        self.root.bind('<Control-s>', self.saveFile)
        self.ScrollBar.pack(side=RIGHT,fill=Y)
        self.ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.ScrollBar.set,insertbackground="#28780b",selectbackground="#254f16", inactiveselectbackground="#254f16")
        filei = open(self.file,"r",newline="")
        self.TextArea.insert(1.0,filei.read())
        filei.close()
    def quitApplication(self):
        self.root.destroy()
    def saveFile(self, *karg):
        file = open(self.file,"w",newline="")
        file.write(self.TextArea.get(1.0,END))
        file.close()
        self.root.title(os.path.basename(self.file))
    def run(self):
        self.root.mainloop()
