'''
Created on Feb 24, 2016

@author: jokirby
'''
import tkinter as tk
from Controls import Controls

class Display(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        cr = Controls()
        
        i = 0
        for button in iter(sorted(cr.button)):
            print(button)
            cr.button[button].grid(row=int(i/3),column=int(i%3))
            i += 1
        





root = tk.Tk()
app = Display(master=root)
app.mainloop()