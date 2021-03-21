import os
from os import path
import tkinter as tk
from subprocess import run
from tkinter import ttk
from tkinter import simpledialog
from shutil import rmtree, move
import time
import sys
from filetool import FileC
from idle import Idle
from Commands.console import Consola
from sitanInterpreteur import Interpret
import datetime as dt
from time import sleep
from PIL import Image, ImageTk
sys.path.append("..")
from ApplicationsMain.TextPad import TextNote

class Inter:
    def __init__(self,user):
        self.C = Consola()
        self.baseimg = None
        self.bg = "black"
        self.fg = "white"
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.path = self.path[self.path.find("\O\\") + 1 : :]
        self.timer = 0
        self.parent_iid = []
        self.notend = True
        self.user = user
        self.root=tk.Tk()
        self.root.config(background="#202020")
        self.root.geometry(f"{int(self.root.winfo_screenwidth())}x{int(self.root.winfo_screenheight())}")
        self.root.attributes('-fullscreen', True)
        self.f=tk.Frame(self.root,background="#202020")
        self.rawdata = open("./settingsdata.db", "r", newline="").read().split("#")
        for lines in self.rawdata:
            if "bg" in tuple(lines.split(","))[0]:
                self.bg = tuple(lines.split(","))[1]
            elif "fg" in tuple(lines.split(","))[0]:
                self.fg = tuple(lines.split(","))[1]
    def centerstart(self,event):
        try:
            self.centermenu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.centermenu.grab_release()
    def popup(self,event):
        self.iid = self.tv.identify_row(event.y)
        if self.iid:
                # mouse pointer over item
            self.tv.selection_set(self.iid)
            try:
                self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
            finally:
                self.popup_menu.grab_release()
        else:
            pass

    def traverse_dir(self,parent,path):
        for d in os.listdir(path):
            full_path=os.path.join(path,d)
            isdir = os.path.isdir(full_path)
            if isdir:
                id=self.tv.insert(parent,'end',text=d,values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(full_path))),"Folder",""),tags=('folder',),open=False)
            else:
                id=self.tv.insert(parent,'end',text=d,values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(full_path))),"File",f"{os.path.getsize(full_path)} octets"),tags=('file',),open=False)
            if isdir:
                self.traverse_dir(id,full_path)
    def delete_selected(self):
        if self.iid:
            self.parent_iid,self.newlist = [],[]
            self.parent_iid.append(self.tv.parent(self.iid))
            self.nb = 0
            while self.notend:
                if self.tv.parent(self.parent_iid[self.nb]) == "":
                    break
                self.parent_iid.append(self.tv.parent(self.parent_iid[self.nb]))
                self.nb += 1
            for obj in self.parent_iid:
                self.newlist.append(self.tv.item(obj)['text'])
            self.newlist.reverse()
            self.back = '\\'

            try:
                os.remove(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}")
                self.tv.delete(self.iid)
            except:
                try:
                    os.rmdir(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}")
                    self.tv.delete(self.iid)
                except:
                    try:
                       rmtree(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}")
                       self.tv.delete(self.iid)
                    except Exception as error:
                        answer = simpledialog.messagebox.askyesno(f"{error}", "Do you want to try that again?")
                        if answer:
                            while answer:
                                try:
                                    os.remove(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}")
                                    self.tv.delete(self.iid)
                                    break
                                except:
                                    try:
                                        os.rmdir(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}")
                                        self.tv.delete(self.iid)
                                        break
                                    except:
                                        try:
                                            rmtree(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}")
                                            self.tv.delete(self.iid)
                                            break
                                        except Exception as error:
                                            answer = False
                                            answer = simpledialog.messagebox.askyesno(f"{error}", "Do you want to try that again?")

    def createin_selected(self):
        if self.iid:
            self.parent_iid,self.newlist = [],[]
            self.parent_iid.append(self.tv.parent(self.iid))
            self.nb = 0
            while self.notend:
                if self.tv.parent(self.parent_iid[self.nb]) == "":
                    break
                self.parent_iid.append(self.tv.parent(self.parent_iid[self.nb]))
                self.nb += 1
            for obj in self.parent_iid:
                self.newlist.append(self.tv.item(obj)['text'])
            self.newlist.reverse()
            self.back = '\\'
            try:
                if os.path.isdir(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}"):
                    if os.path.isfile(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}{self.back}new.empty"):
                        simpledialog.messagebox.showerror("Error", f"new.empty already exist in this folder !")
                    else:
                        open(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}{self.back}new.empty","w+")
                        A = self.tv.insert(self.iid,'end',text="new.empty",values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}{self.back}new.empty"))),"File",str(os.path.getsize(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}{self.back}new.empty")) + ' octets'),tags=('file',))
            except Exception as error:
                simpledialog.messagebox.showerror("Error", f"{error}")
    def rename_selected(self):
        if self.iid:
            user_input = simpledialog.askstring("New name", "Enter a folder name")
            if user_input is not None:
                self.parent_iid,self.newlist = [],[]
                self.parent_iid.append(self.tv.parent(self.iid))
                self.nb = 0
                while self.notend:
                    if self.tv.parent(self.parent_iid[self.nb]) == "":
                        break
                    self.parent_iid.append(self.tv.parent(self.parent_iid[self.nb]))
                    self.nb += 1
                for obj in self.parent_iid:
                    self.newlist.append(self.tv.item(obj)['text'])
                self.newlist.reverse()
                self.back = '\\'
                try:
                    os.rename(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}",f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{user_input}")
                    if os.path.isfile(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{user_input}"):
                        self.tv.item(self.iid ,text=user_input,values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{user_input}"))),"File",str(os.path.getsize(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{user_input}")) + ' octets'),tags=('file',))
                    else:
                        self.tv.item(self.iid ,text=user_input,values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{user_input}"))),"Folder",""),tags=('folder',))
                except Exception as error:
                    simpledialog.messagebox.showerror("Error", f"{error}")

    def move_selected(self):
        if self.iid:
            user_input = simpledialog.askstring("Path", "Enter a Path to move ''in your user''")
            if user_input is not None:
                self.parent_iid,self.newlist = [],[]
                self.parent_iid.append(self.tv.parent(self.iid))
                self.nb = 0
                while self.notend:
                    if self.tv.parent(self.parent_iid[self.nb]) == "":
                        break
                    self.parent_iid.append(self.tv.parent(self.parent_iid[self.nb]))
                    self.nb += 1
                for obj in self.parent_iid:
                    self.newlist.append(self.tv.item(obj)['text'])
                self.newlist.reverse()
                self.back = '\\'
                listecherche = [obj for obj in user_input.split("\\")]
                truc = self.tv.get_children(self.tv.get_children()[0])
                nbb = 0
                Notfind = True
                while Notfind:
                    for m in truc:
                        if listecherche[nbb] == self.tv.item(m)['text']:
                            if listecherche[nbb] == listecherche[-1]:
                                Notfind = False
                                self.idfind = m
                            else:
                                nbb += 1
                                truc = self.tv.get_children([m])
                                break
                    if nbb > 10000:
                        break
                try:
                    move(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}",f"..{self.back}UserS{self.back}{self.user}{self.back}{user_input}")
                    if os.path.isfile(f"..{self.back}UserS{self.back}{self.user}{self.back}{user_input}"):
                        self.tv.insert(self.idfind,'end',text=self.tv.item(self.iid)['text'],values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..{self.back}UserS{self.back}{self.user}{self.back}{user_input}"))),"File",str(os.path.getsize(f"..{self.back}UserS{self.back}{self.user}{self.back}{user_input}")) + ' octets'),tags=('file',))
                    else:
                        self.tv.insert(self.idfind,'end',text=self.tv.item(self.iid)['text'],values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..{self.back}UserS{self.back}{self.user}{self.back}{user_input}"))),"Folder",""),tags=('folder',))
                    self.tv.delete(self.iid)
                except Exception as error:
                    simpledialog.messagebox.showerror("Error", f"{error}")
    def createfolder_selected(self):
        if self.iid:
            self.parent_iid,self.newlist = [],[]
            self.parent_iid.append(self.tv.parent(self.iid))
            self.nb = 0
            while self.notend:
                if self.tv.parent(self.parent_iid[self.nb]) == "":
                    break
                self.parent_iid.append(self.tv.parent(self.parent_iid[self.nb]))
                self.nb += 1
            for obj in self.parent_iid:
                self.newlist.append(self.tv.item(obj)['text'])
            self.newlist.reverse()
            self.back = '\\'
            try:
                if os.path.isdir(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}"):
                    os.mkdir(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}{self.back}newfolder")
                    A = self.tv.insert(self.iid,'end',text="newfolder",values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}{self.back}newfolder"))),"Folder",""),tags=('folder',))
            except Exception as error:
                simpledialog.messagebox.showerror("Error", f"{error}")
    def edit(self):
        if self.iid:
            self.parent_iid,self.newlist = [],[]
            self.parent_iid.append(self.tv.parent(self.iid))
            self.nb = 0
            while self.notend:
                if self.tv.parent(self.parent_iid[self.nb]) == "":
                    break
                self.parent_iid.append(self.tv.parent(self.parent_iid[self.nb]))
                self.nb += 1
            for obj in self.parent_iid:
                self.newlist.append(self.tv.item(obj)['text'])
            self.newlist.reverse()
            self.back = '\\'
            try:
                if os.path.isfile(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}"):
                    TextNote(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}").run()
            except Exception as error:
                simpledialog.messagebox.showerror("Error", f"{error}")
    def reset_timer(self, event=None):
        self.timer=0

    def open_selected(self):
        if self.iid:
            self.parent_iid,self.newlist = [],[]
            self.parent_iid.append(self.tv.parent(self.iid))
            self.nb = 0
            while self.notend:
                if self.tv.parent(self.parent_iid[self.nb]) == "":
                    break
                self.parent_iid.append(self.tv.parent(self.parent_iid[self.nb]))
                self.nb += 1
            for obj in self.parent_iid:
                self.newlist.append(self.tv.item(obj)['text'])
            self.newlist.reverse()
            self.back = '\\'
            try:
                if os.path.isfile(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}"):
                    if self.tv.item(self.iid)['text'][-4:] == ".sit":
                        resultsc = Interpret().make(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}")
                        for toright in resultsc:
                            self.t.config(state="normal")
                            self.t.insert(tk.END,f"{str(toright)}\n")
                            self.t.see(tk.END)
                            self.t.config(state="disabled")
                    else:
                        FileC(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}").lauchapp()
                elif os.path.isdir(f"..{self.back}{f'{self.back}'.join(self.newlist)}{self.back}{self.tv.item(self.iid)['text']}"):
                    if self.tv.item(self.iid)['open'] == True:
                        self.tv.item(self.iid, open=False)
                    else:
                        self.tv.item(self.iid, open=True)
                else: pass
            except Exception as error:
                simpledialog.messagebox.showerror("Error", f"{error}")

    def update_clock(self):
        self.timer+=1
        self.root.after(1000, self.update_clock)
        if self.timer == 60:
            Idle().show()
            self.root.after(1000, self.update_clock)

    def enter(self,event=None):
        self.t.config(state="normal")
        self.t.insert(tk.END,f"<{self.path}> {self.text1.get()}\n")
        if self.text1.get() == "clear":
            self.t.delete('1.0', 'end')
            try:
                for lines in self.rawdata:
                    if "baseimg" in tuple(lines.split(","))[0]:
                        self.baseimg = tuple(lines.split(","))[1]
                        break
                imgtoopen = Image.open(self.baseimg)
                copy= imgtoopen.copy()
                imgtoopen = copy.resize((431, 749))
                imported = ImageTk.PhotoImage(imgtoopen)
                self.t.image_create("1.0", image=imported)
                self.t.image = imported
            except:
                pass
        elif self.text1.get()[:5] == "color":
            try:
                if self.text1.get()[6:8] == "fg":
                    Color = self.text1.get()[9:]
                    self.t.config(fg=Color)
                    self.i.config(fg=Color)
                    self.t.insert(tk.END,"\n")
                elif self.text1.get()[6:8] == "bg":
                    Color = self.text1.get()[9:]
                    self.t.config(bg=Color)
                    self.i.config(bg=Color)
                    self.t.insert(tk.END,"\n")
                else:
                    self.t.insert(tk.END,"\n")
            except Exception as error:
                self.t.insert(tk.END,f"{error}\n")
        elif self.text1.get()[:6] == "imgset":
            if self.text1.get()[-4:] == ".jpg" or self.text1.get()[-4:] == ".png" or self.text1.get()[-4:] == ".gif" or self.text1.get()[-5:] == ".jpeg":
                if self.path == "O\\SystemUnit":
                    try:
                        imgtoopen = Image.open(self.text1.get()[7:])
                        copy= imgtoopen.copy()
                        imgtoopen = copy.resize((431, 749))
                        imported = ImageTk.PhotoImage(imgtoopen)
                        self.t.image_create("1.0", image=imported)
                        self.t.image = imported
                    except Exception as error:
                        self.t.insert(tk.END,f"{error}\n")
                else:
                    try:
                        try:
                            imgtoopen = Image.open(f"{self.path}/{self.text1.get()[7:]}")
                        except:
                            imgtoopen = Image.open(f"{self.path}\\{self.text1.get()[7:]}")
                        copy= imgtoopen.copy()
                        imgtoopen = copy.resize((431, 749))
                        imported = ImageTk.PhotoImage(imgtoopen)
                        self.t.image_create("1.0", image=imported)
                        self.t.image = imported
                    except Exception as error:
                        self.t.insert(tk.END,f"{error}\n")

        elif self.text1.get()[:6] == "dirset":
            if os.path.isdir(self.text1.get()[7:]):
                self.path=self.text1.get()[7:]
                self.t.insert(tk.END,"\n")
            else:
                self.t.insert(tk.END,"No Such directory !\n")
        elif self.text1.get()[:5] == "debug":
            self.rawdata = open("./settingsdata.db", "r", newline="").read().split("#")
            self.t.delete('1.0', 'end')
            for child in self.tv.get_children():
                self.tv.delete(child)
            directory=f'../Users/{self.user}'
            node=self.tv.insert('','end',text=f".\\UserS\\{self.user}",values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..\\UserS\\{self.user}"))),"Folder",""),tags=('folder',),open=True)
            path=os.path.abspath(directory)
            self.traverse_dir(node,path)
            self.t.see(tk.END)
            self.path = "O\\SystemUnit"
            try:
                self.t.config(state="disabled",background=self.bg,fg=self.fg,font=("Consolas"))
            except:
                try:
                    self.t.config(state="disabled",background=f"#{self.bg}",fg=f"#{self.fg}",font=("Consolas"))
                except:
                    try:
                        self.t.config(state="disabled",background=f"#{self.bg}",fg=self.fg,font=("Consolas"))
                    except:
                        try:
                            self.t.config(state="disabled",background=self.bg,fg=f"#{self.fg}",font=("Consolas"))
                        except:
                            self.t.config(state="disabled",background="black",fg="white",font=("Consolas"))
            self.t.pack(side=tk.TOP,anchor="w")
            try:
                self.i.config(background=self.bg,fg=self.fg,font=("Consolas"),insertbackground="white")
            except:
                try:
                    self.i.config(background=f"#{self.bg}",fg=self.fg,font=("Consolas"),insertbackground="white")
                except:
                    try:
                        self.i.config(background=self.bg,fg=f"#{self.fg}",font=("Consolas"),insertbackground="white")
                    except:
                        try:
                            self.i.config(background=f"#{self.bg}",fg=f"#{self.fg}",font=("Consolas"),insertbackground="white")
                        except:
                            self.i.config(background="black",fg="white",font=("Consolas"),insertbackground="white")
            try:
                for lines in self.rawdata:
                    if "baseimg" in tuple(lines.split(","))[0]:
                        self.baseimg = tuple(lines.split(","))[1]
                        break
                imgtoopen = Image.open(self.baseimg)
                copy= imgtoopen.copy()
                imgtoopen = copy.resize((431, 749))
                imported = ImageTk.PhotoImage(imgtoopen)
                self.t.image_create("1.0", image=imported)
                self.t.image = imported
            except:
                pass
        else:
            if self.path == "O\\SystemUnit":
                self.t.insert(tk.END,f"{str(self.C.sortcommand(self.text1.get()))}\n")
            else:
                self.t.insert(tk.END,f"{str(self.C.sortcommand(self.text1.get(),self.path))}\n")
            if self.text1.get()[1:3] == "fs":
                for child in self.tv.get_children():
                    self.tv.delete(child)
                directory=f'../Users/{self.user}'
                node=self.tv.insert('','end',text=f".\\UserS\\{self.user}",values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..\\UserS\\{self.user}"))),"Folder",""),tags=('folder',),open=True)
                path=os.path.abspath(directory)
                self.traverse_dir(node,path)
        self.t.see(tk.END)
        self.t.config(state="disabled")
        self.i.delete(0, 'end')

    def reload(self):
        for child in self.tv.get_children():
            self.tv.delete(child)
        directory=f'../Users/{self.user}'
        node=self.tv.insert('','end',text=f".\\UserS\\{self.user}",values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..\\UserS\\{self.user}"))),"Folder",""),tags=('folder',),open=True)
        path=os.path.abspath(directory)
        self.traverse_dir(node,path)
    def timec(self):
        self.cB.config(text=f"{dt.datetime.now():%H:%M}\n{dt.datetime.now():%a, %b %d %Y}",fg="#a3a0a0",font=("Courier"))
        self.cB.after(1000, self.timec)
    def exiti(self):
        self.root.destroy()
    def startDesk(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        self.statusbar = tk.Label(self.root,bg="#121211" , bd=0, relief=tk.SUNKEN, anchor=tk.W,height="3")
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.cB=tk.Label(self.statusbar, text=f"{dt.datetime.now():%H:%M}\n{dt.datetime.now():%a, %b %d %Y}",bg="#121211")
        self.B1 = tk.Button(self.statusbar, text="#",background="#1f3834",foreground='white',width="4",relief=tk.FLAT,bd="0")
        self.B1.config(activebackground=self.B1.cget('background'),activeforeground=self.B1.cget('foreground'))
        self.tv=ttk.Treeview(self.f,padding=(2, 2, 2, 2),height=35)
        ybar=tk.Scrollbar(self.f,orient=tk.VERTICAL,command=self.tv.yview)
        self.tv.configure(yscroll=ybar.set)
        directory=f'../Users/{self.user}'
        self.tv["columns"]=("one","two","three")
        self.tv.column("#0", width=270, minwidth=270, stretch=tk.NO)
        self.tv.column("one", width=150, minwidth=150, stretch=tk.NO)
        self.tv.column("two", width=400, minwidth=200, stretch=tk.NO)
        self.tv.column("three", width=80, minwidth=50, stretch=tk.NO)
        self.tv.heading("#0",text="Name",anchor=tk.W)
        self.tv.heading("one", text="Date modified",anchor=tk.W)
        self.tv.heading("two", text="Type",anchor=tk.W)
        self.tv.heading("three", text="Size",anchor=tk.W)
        path=os.path.abspath(directory)
        node=self.tv.insert('','end',text=f".\\UserS\\{self.user}",values=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f"..\\UserS\\{self.user}"))),"Folder",""),tags=('folder',),open=True)
        self.centermenu = tk.Menu(self.B1, tearoff=0)
        self.centermenu.add_command(label="Exit",command=self.exiti)
        self.B1.bind("<Button-3>", self.centerstart)
        self.B1.bind("<Button-1>", self.centerstart)
        self.popup_menu = tk.Menu(self.root, tearoff=0)
        self.popup_menu.add_command(label="Open",command=self.open_selected)
        self.popup_menu.add_command(label="Edit",command=self.edit)
        self.popup_menu.add_command(label="New File",command=self.createin_selected)
        self.popup_menu.add_command(label="New Folder",command=self.createfolder_selected)
        self.popup_menu.add_command(label="Rename",command=self.rename_selected)
        self.popup_menu.add_command(label="Move",command=self.move_selected)
        self.popup_menu.add_command(label="Reload",command=self.reload)
        self.popup_menu.add_command(label="Delete",command=self.delete_selected)
        self.tv.bind("<Button-3>", self.popup)
        self.root.bind_all('<Any-KeyPress>', self.reset_timer)
        self.root.bind_all('<Any-ButtonPress>', self.reset_timer)
        self.root.after(1000, self.update_clock)
        ybar.pack(side=tk.RIGHT,fill=tk.Y)
        self.f.pack(side=tk.RIGHT,anchor="n")
        self.tv.pack(side=tk.RIGHT,anchor="n",padx=(0,0))
        self.image = Image.open("./images/origin.jpg")
        self.t = tk.Text(width="50")
        self.text1 = tk.StringVar()
        self.i = tk.Entry(width="50",textvariable=self.text1)
        try:
            self.t.config(state="disabled",background=self.bg,fg=self.fg,font=("Consolas"))
        except:
            try:
                self.t.config(state="disabled",background=f"#{self.bg}",fg=f"#{self.fg}",font=("Consolas"))
            except:
                try:
                    self.t.config(state="disabled",background=f"#{self.bg}",fg=self.fg,font=("Consolas"))
                except:
                    try:
                        self.t.config(state="disabled",background=self.bg,fg=f"#{self.fg}",font=("Consolas"))
                    except:
                        self.t.config(state="disabled",background="black",fg="white",font=("Consolas"))
        self.t.pack(side=tk.TOP,anchor="w")
        try:
            self.i.config(background=self.bg,fg=self.fg,font=("Consolas"),insertbackground="white")
        except:
            try:
                self.i.config(background=f"#{self.bg}",fg=self.fg,font=("Consolas"),insertbackground="white")
            except:
                try:
                    self.i.config(background=self.bg,fg=f"#{self.fg}",font=("Consolas"),insertbackground="white")
                except:
                    try:
                        self.i.config(background=f"#{self.bg}",fg=f"#{self.fg}",font=("Consolas"),insertbackground="white")
                    except:
                        self.i.config(background="black",fg="white",font=("Consolas"),insertbackground="white")
        self.i.pack(side=tk.TOP,anchor="w")
        self.i.bind('<Return>', self.enter)
        try:
            for lines in self.rawdata:
                if "baseimg" in tuple(lines.split(","))[0]:
                    self.baseimg = tuple(lines.split(","))[1]
                    break
            imgtoopen = Image.open(self.baseimg)
            copy= imgtoopen.copy()
            imgtoopen = copy.resize((431, 749))
            imported = ImageTk.PhotoImage(imgtoopen)
            self.t.image_create("1.0", image=imported)
            self.t.image = imported
        except:
            pass
        self.traverse_dir(node,path)
        style.configure("Treeview", background="#202020",fieldbackground="#202020")
        self.cB.pack(side='right')
        self.B1.pack(side='left',fill="y")
        self.timec()
        self.root.mainloop()