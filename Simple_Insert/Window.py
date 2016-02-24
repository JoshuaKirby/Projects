'''
Created on Feb 24, 2016

@author: jokirby
'''
import csv
import tkinter as tk
import time

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.inString = tk.StringVar()
        
        self.input = tk.Entry(self)
        self.input["textvariable"] = self.inString
        self.input.pack(side="top")
        
        self.submit = tk.Button(self)
        self.submit["text"] = "Submit"
        self.submit["command"] = self.readIn
        self.submit.pack(side="top")
        
        
        
    def readIn(self):
        with open('data.csv', 'a') as csvfile:
            csvWriter = csv.writer(csvfile, delimiter=' ',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow([time.localtime(),self.inString.get()])
            
        self.inString.set("")
        
        
        with open('data.csv', 'rb') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=' ', quotechar='|')

root = tk.Tk()
app = Window(master=root)
app.mainloop()