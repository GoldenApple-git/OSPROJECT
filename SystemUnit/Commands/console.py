#!/usr/bin/env python
import os
from os import path
import re
import time
import sys
try:
    from prefix import prefix
    from func.fs import Fs
    from func.regc import SetData
    from func.help import ShowCmd
    from dark.tokenplay import TokenAuthUse
    from dark.accountdb import DataManager
    if prefix().ispremium():
        from dark.premiumclass.nhdl import DownNhentai, Hreader, ListeAll, DeleteOne
    from dark.panic import SelfEnd
except:
    from Commands.prefix import prefix
    from Commands.func.fs import Fs
    from Commands.func.regc import SetData
    from Commands.func.help import ShowCmd
    from Commands.dark.tokenplay import TokenAuthUse
    from Commands.dark.accountdb import DataManager
    if prefix().ispremium():
        from Commands.dark.premiumclass.nhdl import DownNhentai, Hreader, ListeAll, DeleteOne
    from Commands.dark.panic import SelfEnd
sys.path.append("..")
from sitanInterpreteur import Interpret


class Consola:
    def __init__(self,path=None):
        self.I=Interpret()
        self.isActive = True
        if path is None:
            self.path = os.path.dirname(os.path.realpath(__file__))
            self.path = self.path[self.path.find("\O\\") + 1 : self.path.find("\Commands\\") - len("Commands") :]
        else:
            self.path = path

    def sortcommand(self,command=None,path=None):
        if command != None and command != "":
            if command[0] == prefix().findprefix():
                self.t0 = time.time()
                command = command[0 + 1 : :]
                command = tuple(re.split(" ", command))
                if command[0] == "fs":
                    if path is not None:
                        try:
                            if os.path.isdir(f"{path}/{command[2]}") or os.path.isfile(f"{path}/{command[2]}"):
                                self.conc = Fs(command[1],f"{path}/{command[2]}",f"{path}/{command[3]}").fssort()
                            elif os.path.isdir(f"{path}\\{command[2]}") or os.path.isfile(f"{path}\\{command[2]}"):
                                self.conc = Fs(command[1],f"{path}\\{command[2]}",f"{path}\\{command[3]}").fssort()
                            else:
                                return f"No such file or directory !"
                        except:
                            try:
                                if os.path.isdir(f"{path}/{command[2]}") or os.path.isfile(f"{path}/{command[2]}"):
                                    self.conc = Fs(command[1],f"{path}/{command[2]}").fssort()
                                elif os.path.isdir(f"{path}\\{command[2]}") or os.path.isfile(f"{path}\\{command[2]}"):
                                    self.conc = Fs(command[1],f"{path}\\{command[2]}").fssort()
                                else:
                                    return f"No such file or directory !"
                            except:
                                try:
                                    self.conc = Fs(command[1]).fssort()
                                except IndexError:
                                    return "No argument provided"
                                except Exception as error:
                                    return f"error : {error}"
                    else:
                        try:
                            self.conc = Fs(command[1],command[2],command[3]).fssort()
                        except:
                            try:
                                self.conc = Fs(command[1],command[2]).fssort()
                            except:
                                try:
                                    self.conc = Fs(command[1]).fssort()
                                except IndexError:
                                    return "No argument provided"
                                except Exception as error:
                                    return f"error : {error}"
                elif command[0] == "exit":
                    exit(0)

                elif command[0] == "setdefault":
                    try:
                        self.conc = SetData((command[1],command[2])).enddata()
                    except IndexError:
                        return "No arguments or Invalid arguments numbers !"
                    except Exception as error:
                        return f"error : {error}"
                elif command[0] == "cmds":
                    self.conc = ShowCmd().shwohelp()
                elif command[0] == "dark":
                    if command[1] == "token":
                        if command[2] == "-a":
                            self.conc = TokenAuthUse().addtoken(command[3],command[4])
                        elif command[2] == "-r":
                            try:
                                self.conc = TokenAuthUse().readtoken()
                            except Exception as error:
                                return error
                        elif command[2] == "help":
                            return "Arguments token : \n -r : read tokens \n -a : add tokens"
                        else:
                            return "Invalid argument"
                    elif command[1] == "datahook":
                        if command[2] == "-a":
                            try:
                                self.conc = DataManager().adddata(command[3],command[4],command[5])
                            except:
                                try:
                                    self.conc = DataManager().adddata(command[3],command[4])
                                except:
                                    try:
                                        self.conc = DataManager().adddata(command[3])
                                    except:
                                        return "No argument !"
                        elif command[2] == "-r":
                            self.conc = DataManager().readdata()
                        elif command[2] == "help":
                            return "Arguments datahook : \n -r : read datas \n -a : add datas"
                        else:
                            return "Invalid argument"
                    else:
                        return "No valid dark command given !"
                elif command[0] == "admin":
                    try:
                        if command[1] == "-n":
                            try:
                                if prefix().ispremium():
                                    self.conc = DownNhentai(str(command[2])).downimg(str(command[2]))
                                else:
                                    return "Not premium !"
                            except Exception as error:
                                return error
                        elif command[1] == "-nr":
                            Hreader(str(command[2])).showimage()
                        elif command[1] == "-nl":
                            self.conc = ListeAll().resultsend()
                        elif command[1] == "-nd":
                            self.conc = DeleteOne(str(command[2])).startdel()
                        elif command[1] == "help":
                            return "Arguments admin : \n -n : NHentai download \n -nr : Read Nhentai manga \n -nl : list all \n -nd : delete a NH manga"
                        else:
                            return "No valid admin command given !"
                    except IndexError:
                        return "Arguments requires"
                    except Exception as error:
                        return error
                elif command[0] == "urg":
                    if command[1] == "1":
                        SelfEnd().active()
                        exit(0)
                    elif command[1] == "0":
                        exit(0)
                    else:
                        return "No valid panic value !"
                else:
                    return "Not a valid Command !"
                self.t1 = time.time()
                self.total = self.t1-self.t0
                return f"Action made in {self.total} s\n{self.conc}"
            else:
                return self.I.do(command)
        else: return ""