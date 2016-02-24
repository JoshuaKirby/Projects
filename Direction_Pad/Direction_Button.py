'''
Created on Feb 24, 2016

@author: jokirby
'''
import tkinter as tk

class DButton(tk.Button):
    
    def __init__(self,img,direction):
        super.image = img;
        super.command = self.onClick(direction)
        
    def onClick(self, direction):
        print(direction)
        
    __name__ = "DButton"
    