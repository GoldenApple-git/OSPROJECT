class Varx:
    def __init__(self,value,var):
        self.value = value
        self.var = var

    def calc(self):
        return {str(self.var):self.value}