import os
import time
from shutil import rmtree

class Fs:
    def __init__(self,arg,path=None,argsnew=None):
        self.path=path
        self.arg=arg
        self.argsnew=argsnew

    def fssort(self):
        if self.arg == "-d":
            return self.fsd()
        if self.arg == "-c":
            return self.fsc()
        if self.arg == "-fd":
            return self.fsfd()
        if self.arg == "-fc":
            return self.fsfc()
        if self.arg == "-r":
            return self.fsrename()
        if self.arg == "help":
            return "Arguments fs : \n -d : delete files \n -c : create files \n -fd : delete folders \n -fc : create folders \n -r : rename files/folders"

    def fsd(self):
        if self.path is None:
            return "No path or file given !"
        else:
            if os.path.exists(self.path):
                os.remove(self.path)
                return "Sucess"
            else:
                return "The file does not exist"

    def fsc(self):
        if self.path is None:
            return "No path or file name given !"
        else:
            if os.path.exists(self.path):
                return "File already exist !"
            open(self.path,"w+")
            return "Sucess"

    def fsfc(self):
        if self.path is None:
            return "No path or folder name given !"
        else:
            if os.path.exists(self.path):
                return "folder already exist !"
            else:
                os.mkdir(self.path)
                return "Sucess"

    def fsfd(self):
        if self.path is not None:
            if os.path.exists(self.path):
                rmtree(self.path)
                return "Sucess"
            else:
                return "The folder does not exist"
        else:
            return "No path or folder name given !"

    def fsrename(self):
        if self.path is None:
            return "No path or file/folder given !"
        else:
            if os.path.exists(self.path):
                os.rename(self.path,self.argsnew)
                return "Sucess"
            else:
                return "The file/folder does not exist"