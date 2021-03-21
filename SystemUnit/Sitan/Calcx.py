class Calcx:
    def __init__(self,var,*arg):
        self.var1 = var
        self.args = arg
        self.final = []
        self.change = self.args[0]

    def getnb(self,nb):
        if type(nb) != list:
            self.final = nb.split(' ')
    def calc(self):
        if type(self.args[0]) == list:
            for nb in self.args:
                self.getnb(nb)
            for f in range(len(self.final)):
                if self.final[f].isalpha():
                    if self.final[f] != "+" or "-" or "*" or "/":
                        for obj in self.change:
                            for key,value in obj.items():
                                if self.final[f] == key:
                                    self.final[f] = value
            self.end = ''.join(self.final)
            return {self.var1:str(eval(self.end))}

        else:
            print("no")
            return {self.var1:eval(self.args[0])}
