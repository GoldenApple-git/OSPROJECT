from tkinter import *
import winsound

class MusicPlay:
    def __init__(self, file):
        self.root = Tk()
        self.file = file
    def playsound(self):
        winsound.PlaySound(self.file, winsound.SND_FILENAME)

    def load(self):
        Button(self.root,text="Play",command=self.playsound).pack()
        self.root.mainloop()