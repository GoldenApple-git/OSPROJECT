import sys
import os
sys.path.append("..")
from ApplicationsMain.PhotoView import ImgReader
from ApplicationsMain.TextPad import TextNote
from ApplicationsMain.Musix import MusicPlay

class FileC:
    def __init__(self,file):
        self.file = file

    def lauchapp(self):
        self.trifile()
        if self.ext == "txt":
            TextNote(self.file).run()
        elif self.ext == "jpg" or self.ext == "png" or self.ext == "jpeg" or self.ext == "gif":
            ImgReader(self.file).showimage()
        elif self.ext == "mp3" or self.ext == "wav":
            MusicPlay(self.file).load()
        elif self.ext == "exe":
            os.startfile(self.file)
        else:
            pass

    def trifile(self):
        self.ext = self.file.split(".")[-1]