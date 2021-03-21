from compiles import Compile
import os
from Interface import Inter

class Launch:
    def __init__(self, user):
        self.user = user

    def DecompileSession(self):
        Compile().decompilfile(f"../LocalData/Account/{self.user}.db")

    def start(self):
        if os.path.exists(f"../UserS/{self.user}"):
            #self.DecompileSession()
            I = Inter(self.user)
            I.startDesk()
            #Compile(self.user).compilefile(self.user)
        else:
            os.mkdir(f"../UserS/{self.user}/")
            I = Inter(self.user)
            I.startDesk()
