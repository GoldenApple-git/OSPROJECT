class SetData:
    def __init__(self,param):
        self.param = param
        self.text = open("./settingsdata.db", "a", newline="")
        self.get = open("./settingsdata.db", "r", newline="").read().split("#")

    def enddata(self):
        if self.param[0] == "account":
            return "You can't do that !"
        for letter in self.param[0]:
            if letter == "#":
                return "No '#' allowed"
            elif letter == ",":
                return "No ',' allowed"
        for letter in self.param[1]:
            if letter == "#":
                return "No '#' allowed"
            elif letter == ",":
                return "No ',' allowed"
        p=0
        find = False
        for lines in self.get:
            if self.param[0] in tuple(lines.split(","))[0]:
                datas = open("./settingsdata.db", "r", newline="").readlines()
                if datas[p][-2:] == "#\n":
                    datas[p] = f"{self.param[0]},{self.param[1]}#\n"
                else:
                    datas[p] = f"{self.param[0]},{self.param[1]}"
                find = True
            p+=1
        if find == False:
            self.text.write(f"#\n{self.param[0]},{self.param[1]}")
            return "Key and value add !"
        else:
            open("./settingsdata.db", "w", newline="").writelines(datas)
            return "Key and value replace !"