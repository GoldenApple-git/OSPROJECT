import os

class TokenAuthUse:
    def __init__(self):
        try:
            self.get = open("./authtoken.db", "r", newline="").read().split("#")
        except:
            self.get = open("./Commands/dark/authtoken.db", "r", newline="").read().split("#")
        self.end=[]
    def addtoken(self,typ,token):
        if os.path.isfile("./authtoken.db"):
            open("./authtoken.db", "a", newline="").write(f"#\n{typ},{token}")
        else:
            open("./Commands/dark/authtoken.db", "a", newline="").write(f"#\n{typ},{token}")
        return f"token : {token} succefuly add with type : {typ}"

    def readtoken(self):
        for lines in self.get:
            self.end.append(tuple(lines.split(","))[0] + ' : ' + tuple(lines.split(","))[1]+'\n')
        return ''.join([i for i in self.end])
