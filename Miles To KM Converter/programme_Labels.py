from tkinter import *
class Labels(Label):
    
    def __init__(self,**kwargs):
        super().__init__()
        if kwargs.get("text") == 0:
            self.value = float(0)
        self.config(text=kwargs.get("text"))
        self.config(text=kwargs.get("value"))
        self.config(font=kwargs.get("font"))
        self.grid(row=kwargs.get("row"), column=kwargs.get("column"))
        
        
    def UpdateTheValue(self,valuegiven):
        self.value = valuegiven*1.60934
        self.config(text=self.value)