from tkinter import *
from PIL import Image, ImageTk

class ImgReader:
    def __init__(self,file):
        self.file = file
        self.apk = Tk()
        self.screenWidth = self.apk.winfo_screenwidth()
        self.screenHeight = self.apk.winfo_screenheight()
        self.apk.title("Image Viewer")
        self.apk.geometry(f"{self.screenWidth}x{self.screenHeight}")
        self.apk.configure(background="#202020")
        self.apk.attributes('-fullscreen', True)

    def resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((self.width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image,master = self.apk)
        self.background.configure(image =  self.background_image)

    def showimage(self):
        self.image = Image.open(self.file)
        self.width, self.height = self.image.size
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image,master = self.apk)
        self.background = Label(self.apk, image=self.background_image)
        self.background.configure(background="#202020")
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self.resize_image)
        Button(self.background, text="Exit", command=self.apk.destroy,anchor="e").pack()
        self.apk.mainloop()