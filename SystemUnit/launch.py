from connect import Login
from idle import Idle
from register import Reg

class launch:
    def __init__(self):
        self.rawdata = open("./settingsdata.db", "r", newline="").read().split("#")

    def check(self, find=None):
        for lines in self.rawdata:
            if "account" in tuple(lines.split(","))[0]:
                self.start()
                find = True
                break
        if find is None: self.New()

    def start(self):
        I = Idle()
        I.show()
        L = Login()
        L.show()

    def New(self):
        R = Reg()
        R.show()
        I = Idle()
        I.show()
        L = Login()
        L.show()

La = launch()
La.check()
