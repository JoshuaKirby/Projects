'''
Created on Feb 24, 2016

@author: jokirby
'''
import tkinter as tk
from Turn import Turn

class Controls():
    #Data
    direction = {0:"UpLeft",1:"Up",2:"UpRight", \
                 3:"Left",4:"Center",5:"Right", \
                 6:"DownLeft",7:"Down",8:"DownRight"}
    arrow = {0:"",1:"↑",2:"", \
             3:"←",4:"",5:"→", \
             6:"",7:"↓",8:""}
    
    def __init__(self, master=None):
        self.initDirectionButtons()
        
         
    #Methods   
    def initDirectionButtons(self):
        self.button = {0:tk.Button(text=self.arrow[0], command=self.cmdUpLeft), \
                       1:tk.Button(text=self.arrow[1], command=self.cmdUp), \
                       2:tk.Button(text=self.arrow[2], command=self.cmdUpRight), \
                       3:tk.Button(text=self.arrow[3], command=self.cmdLeft), \
                       4:tk.Button(text=self.arrow[4], command=self.cmdCenter), \
                       5:tk.Button(text=self.arrow[5], command=self.cmdRight), \
                       6:tk.Button(text=self.arrow[6], command=self.cmdDownLeft), \
                       7:tk.Button(text=self.arrow[7], command=self.cmdDown), \
                       8:tk.Button(text=self.arrow[8], command=self.cmdDownRight)}    
          
    def command(self,direction):   
        Turn.lastDirection = direction 
        pass
    def cmdUpLeft(self):
        self.command(0)
        pass 
    def cmdUp(self):
        self.command(1)
        pass 
    def cmdUpRight(self):
        self.command(2)
        pass 
    def cmdLeft(self):
        self.command(3)
        pass 
    def cmdCenter(self):
        self.command(4)
        pass 
    def cmdRight(self):
        self.command(5)
        pass 
    def cmdDownLeft(self):
        self.command(6)
        pass 
    def cmdDown(self):
        self.command(7)
        pass 
    def cmdDownRight(self):
        self.command(8)
        pass 