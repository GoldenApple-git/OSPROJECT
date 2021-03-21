try:
    from bs4 import *
    import requests
except:
    exit(0)
import os
from shutil import rmtree
import re
from tkinter import *
from PIL import Image, ImageTk

class DownNhentai:
    def __init__(self,name):
        r = requests.get(f"https://nhentai.xxx/g/{name}")
        soup = BeautifulSoup(r.text, 'html.parser')
        self.images = soup.findAll('img')
        del(self.images[0])
        del(self.images[1])
        try:
            os.mkdir(f"../LocalData/HN")
        except:
            pass
        try:
            os.mkdir(f"../LocalData/HN/{name}")
        except Exception as error:
            print(f"Error can't create : ../LocalData/HN/{name} : {error}")

    def downimg(self,folder_name):
        count = 0
        increm = 0
        if len(self.images) != 0:
            for i, image in enumerate(self.images):
                if (i % 2) == 1:
                    try:
                        image_link = image["data-srcset"]
                    except:
                        try:
                            image_link = image["data-src"]
                        except:
                            try:
                                image_link = image["data-fallback-src"]
                            except:
                                try:
                                    image_link = image["src"]
                                except:
                                    pass
                    try:
                        r = requests.get(image_link).content
                        try:
                            r = str(r, 'utf-8')
                        except UnicodeDecodeError:
                            with open(f"../LocalData/HN/{folder_name}/images{i-increm}.jpg", "wb+") as f:
                                f.write(r)
                            count += 1
                            increm += 1
                    except:
                        pass
                else: count += 1
            return f"[+] fin, bonne lecture ! {round(len(self.images)/2)} Téléchargées."

class Hreader:
    def __init__(self,folder):
        self.folder = folder
        self.files = [f for f in os.listdir(f"../LocalData/HN/{folder}") if os.path.isfile(os.path.join(f"../LocalData/HN/{folder}/", f))]
        self.files.sort(key=lambda f: int(re.sub('\D', '', f)))
        self.apk = Tk()
        self.screenWidth = self.apk.winfo_screenwidth()
        self.screenHeight = self.apk.winfo_screenheight()
        self.apk.title("Hentai Viewer")
        self.apk.geometry(f"{self.screenWidth}x{self.screenHeight}")
        self.apk.configure(background="#202020")
        self.apk.attributes('-fullscreen', True)

    def right(self):
        if self.index < len(self.files)-1:
            self.index+=1
            self.image = Image.open(f"../LocalData/HN/{self.folder}/{self.files[self.index]}")
            self.width, self.height = self.image.size
            self.img_copy= self.image.copy()
            if int(self.width*2) < 410 and int(self.height*2) < 600:
                self.img_copy = self.img_copy.resize((int(self.width*2), int(self.height*2)))
            elif int(self.width*1.5) < 410 and int(self.height*1.5) < 600:
                self.img_copy = self.img_copy.resize((int(self.width*1.5), int(self.height*1.5)))
            self.background_image = ImageTk.PhotoImage(self.img_copy,master = self.apk)
            self.background.configure(image =  self.background_image)
            self.B1.configure(background="#202020")
            self.B2.configure(background="#202020")
            self.B3.configure(background="#202020")

    def left(self):
        if self.index != 0:
            self.index-=1
            self.image = Image.open(f"../LocalData/HN/{self.folder}/{self.files[self.index]}")
            self.width, self.height = self.image.size
            self.img_copy= self.image.copy()
            if int(self.width*2) < 410 and int(self.height*2) < 600:
                self.img_copy = self.img_copy.resize((int(self.width*2), int(self.height*2)))
            elif int(self.width*1.5) < 410 and int(self.height*1.5) < 600:
                self.img_copy = self.img_copy.resize((int(self.width*1.5), int(self.height*1.5)))
            self.background_image = ImageTk.PhotoImage(self.img_copy,master = self.apk)
            self.background.configure(image =  self.background_image)
            self.B1.configure(background="#202020")
            self.B2.configure(background="#202020")
            self.B3.configure(background="#202020")

    def showimage(self):
        self.index=0
        self.image = Image.open(f"../LocalData/HN/{self.folder}/{self.files[self.index]}")
        self.width, self.height = self.image.size
        self.img_copy= self.image.copy()
        if int(self.width*2) < 410 and int(self.height*2) < 600:
            self.img_copy = self.img_copy.resize((int(self.width*2), int(self.height*2)))
        elif int(self.width*1.5) < 410 and int(self.height*1.5) < 600:
            self.img_copy = self.img_copy.resize((int(self.width*1.5), int(self.height*1.5)))
        self.background_image = ImageTk.PhotoImage(self.img_copy,master = self.apk)
        self.background = Label(self.apk, image=self.background_image)
        self.background.configure(background="#202020")
        self.background.pack(fill=BOTH, expand=YES)
        self.B1 = Button(self.background, text="Exit", command=self.apk.destroy,anchor="e",background="#202020",fg='white')
        self.B2 = Button(self.background, text="<", command=self.left,background="#202020",fg='white',width="10",height="10")
        self.B3 = Button(self.background, text=">", command=self.right,background="#202020",fg='white',width="10",height="10")
        self.B1.pack()
        self.B2.pack(side='left', anchor="s")
        self.B3.pack(side='right', anchor="s")
        self.apk.mainloop()

class ListeAll:
    def __init__(self):
        if os.path.isdir(f"../LocalData/HN/"):
            self.folders = [f for f in os.listdir(f"../LocalData/HN/") if os.path.isdir(os.path.join(f"../LocalData/HN/", f))]
            if self.folders == []:
                self.folders = ["No manga !"]
        else: self.folders = ["No manga !"]

    def resultsend(self):
        al = ', '.join([i for i in self.folders])
        return f"allfolders : {al}"

class DeleteOne:
    def __init__(self,folder):
        if os.path.isdir(f"../LocalData/HN/{folder}"):
            self.folder = f"../LocalData/HN/{folder}"
        else:
            self.message = "No manga !"
            self.folder = None

    def startdel(self):
        if self.folder is not None:
            try:
                rmtree(self.folder)
            except Exception as error:
                return error
            return f"{self.folder} as been deleted"
        else:
            return self.message