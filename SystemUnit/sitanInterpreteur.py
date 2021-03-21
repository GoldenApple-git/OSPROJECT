from Sitan import Varx
from Sitan import Osee
from Sitan import PStop
from Sitan import Calcx
import re

class Interpret:
    def __init__(self):
        self.Main = False
        self.p = 0
        self.listes = []

    def make(self, file=None):
        self.end=[]
        if file is not None:
            self.raw = open(file).read().split("#")
            del(self.raw[-1])
            self.raw = map(lambda s: s.strip(), self.raw)
        for code in self.raw:
            code = code.split(":")
            if self.Main == True:
                if code[0] == "Varx":
                    try:
                        self.listes.append(Varx.Varx(code[2],code[1]).calc())
                    except Exception as e:
                        self.end.append(e)
                elif code[0] == "Osee":
                    tour = 0
                    if self.listes == []:
                        self.end.append(Osee.Osee(code[1]).aff())
                    else:
                        for obj in self.listes:
                            tour += 1
                            key, value = list(obj.items())[0]
                            if key == code[1]:
                                self.end.append(Osee.Osee(value).aff())
                                break
                            if tour == len(self.listes):
                                self.end.append(Osee.Osee(code[1]).aff())
                elif code[0] == "Calcx":
                    tour = 0
                    find = 0
                    tocalc = []
                    for obj in self.listes:
                        tour += 1
                        key, value = list(obj.items())[0]
                        if code[2].find(key) != -1:
                            tocalc.append({key:value})
                            find = 1
                        if find == 1:
                            if tour == len(self.listes):
                                self.listes.append(Calcx.Calcx(code[1],tocalc,code[2]).calc())
                                self.listes.reverse()
                                tour += 2
                        elif find == 0:
                            if tour == len(self.listes):
                                self.listes.append(Calcx.Calcx(code[1],code[2]).calc())
                                self.listes.reverse()
                                break
                elif code[0] == "PStop":
                    if 1 < len(code):
                        PStop.PStop(code[1]).stop()
                    else:
                        PStop.PStop().stop()

                elif code[0] == "EndMain":
                    self.Main = False
                elif code[0] == "Main":
                    self.end.append("Already exist Main !")
                else:
                    if code is not None or code != "" or code[0] != " " or code[0] != "\n":
                        self.end.append(f"unknow command on line {self.p + 1}")
            elif code[0] == "Main":
                self.Main = True

            else:
                self.end.append("No Main Found !")

            self.p += 1
        return self.end

    def do(self,code):
        code = code.split(":")
        if self.Main == True:
            if code[0] == "Varx":
                try:
                    self.listes.append(Varx.Varx(code[2],code[1]).calc())
                    self.listes.reverse()
                except Exception as e:
                    return e
                return ""
            elif code[0] == "Osee":
                tour = 0
                if self.listes == []:
                    return Osee.Osee(code[1]).aff()
                else:
                    for obj in self.listes:
                        tour += 1
                        key, value = list(obj.items())[0]
                        if key == code[1]:
                            return Osee.Osee(value).aff()
                            break
                        if tour == len(self.listes):
                            return Osee.Osee(code[1]).aff()
            elif code[0] == "Calcx":
                self.tour = 0
                self.find = 0
                self.tocalc = []
                for obj in self.listes:
                    self.tour += 1
                    key, value = list(obj.items())[0]
                    if code[2].find(key) != -1:
                        self.tocalc.append({key:value})
                        self.find = 1
                    if self.find == 1:
                        if self.tour == len(self.listes):
                            print(self.tocalc)
                            self.listes.append(Calcx.Calcx(code[1],self.tocalc,code[2]).calc())
                            self.listes.reverse()
                            self.tour += 2
                    elif self.find == 0:
                        if self.tour == len(self.listes):
                            self.listes.append(Calcx.Calcx(code[1],code[2]).calc())
                            self.listes.reverse()
                            break
                return ""
            elif code[0] == "PStop":
                if 1 < len(code):
                    PStop.PStop(code[1]).stop()
                else:
                    return "No Time Provided !"
                return ""

            elif code[0] == "EndMain":
                self.Main = False
                return ""
            elif code[0] == "Main":
                return "Main Already exist !"
            else:
                if code is not None or code != "" or code[0] != " " or code[0] != "\n":
                    return f"unknow command on line {self.p + 1}"
        elif code[0] == "Main":
            self.Main = True
            return ""

        else:
            return ""

        self.p += 1


