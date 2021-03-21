class ShowCmd:
    def __init__(self):
        self.cmd = """
Sys Commands [prefix][command] [arg] :
 -cmd : None
 -fs : [arg] [path] ([path2])
 -setdefault : [key] [value]
 -exit : None

Graph/Console Commands [command] [arg] :
 -color : [arg] [colorname/hex(no "#")]
 -clear : None
 -imgset : [path]
 -dirset : [path]
 -debug : None

Sitan Function [function]:[arg] :
 -Main : None
 -EndMain : None
 -PStop : [time]
 -Varx : [variable] [value]
 -Calcx : [varible] [variable/value]
 -Osee : [variable/value]
"""

    def shwohelp(self):
        return self.cmd
