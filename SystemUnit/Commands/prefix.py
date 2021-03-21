class prefix:
    def __init__(self, settingsfilecontent=None):
        if settingsfilecontent is None:
            try:
                self.rawdata = open("../settingsdata.db", "r", newline="").read().split("#")
            except:
                self.rawdata = open("./settingsdata.db", "r", newline="").read().split("#")
        else:
            self.rawdata = settingsfilecontent

    def findprefix(self):
        for lines in self.rawdata:
            if "prefix" in tuple(lines.split(","))[0]:
                self.prefix = tuple(lines.split(","))[1]
                break
        return self.prefix
    
    def ispremium(self):
        self.premium = None
        for lines in self.rawdata:
            if "premium" in tuple(lines.split(","))[0]:
                self.premium = bool(tuple(lines.split(","))[1])
                break
        if self.premium is not None:
            if type(self.premium) == bool:
                return self.premium
            else:
                return False
        else:
            return False

