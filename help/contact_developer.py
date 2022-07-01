
from tkinter import *
from tkinter import messagebox
from webbrowser import open_new

class Help:
    """ Contact the application developer """
    def __init__(self,master):
        self.master = master
        self.menubar = Menu(self.master)
        self.file = Menu(self.menubar)
        self.file.add_command()
        
        self.menubar.add_cascade(label='Developer',command=self.communication)
        self.master.config(menu=self.menubar)
    
    def communication(self):
        open_new('https://www.facebook.com/alaa.jassim.mohammed/')      