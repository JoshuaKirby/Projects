'''
Created on Feb 24, 2016

@author: jokirby
'''
import tkinter as tk

class Window(tk.Frame):
    direction = {0:"UpLeft",1:"Up",2:"UpRight", \
                 3:"Left",4:"Center",5:"Right", \
                 6:"DownLeft",7:"Down",8:"DownRight"}
    arrow = {0:"",1:"↑",2:"", \
             3:"←",4:"",5:"→", \
             6:"",7:"↓",8:""}
    command = {0:onClick(0),1:onClick(1),2:onClick(2), \
             3:onClick(3),4:onClick(4),5:onClick(5), \
             6:onClick(6),7:onClick(7),8:onClick(8)}
    
    #image = {"UpLeft":Image.open("Images/UpLeft.png"),"Up":Image.open("Images/Up.png"),"UpRight":Image.open("Images/UpRight.png"), \
    #         "Left":Image.open("Images/Left.png"),"Center":Image.open("Images/Up.png"),"Right":Image.open("Images/Right.png"), \
    #         "DownLeft":Image.open("Images/DownLeft.png"),"Down":Image.open("Images/Down.png"),"DownRight":Image.open("Images/DownRight.png")}
    button = {}
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        i = 0
        while(i < 3):
            self.columnconfigure(i, minsize = 30)
            self.rowconfigure(i, minsize = 30)
            i = i + 1
        self.createWidgets()
    
    def createWidgets(self):
        #self.button = self.createButtonDict(self.direction)
        self.button = {0:tk.Button(text="a"),1:tk.Button(text="↑"),2:tk.Button(text="c"), \
                 3:tk.Button(text="←"),4:tk.Button(text="●"),5:tk.Button(text="→"), \
                 6:tk.Button(text="g"),7:tk.Button(text="↓"),8:tk.Button(text="i")}
        self.command = {0:self.onClick(0),1:self.onClick(1),2:self.onClick(2), \
             3:self.onClick(3),4:self.onClick(4),5:self.onClick(5), \
             6:self.onClick(6),7:self.onClick(7),8:self.onClick(8)}
        i = 0
        for item in self.button.values():
                item.grid(row = int(i/3),column = int(i%3))
                
                item["command"] = item.onClick(i)
                i = i + 1
    def onClick(self,direction):
         print(direction)   
        
    
    #===========================================================================
    # def createButtonDict(self,direction):
    #     buttons = []
    #     output = {}
    #     i = 0
    #     for arrow in direction:
    #         buttons.append(self.createButton(arrow, None))
    #     for arrow in direction:
    #         output[self.direction[arrow]] = buttons[arrow]
    #         output[self.direction[arrow]]["text"] = self.arrow[i]
    #         i = i + 1
    #     return output
    #         
    # 
    #     
    # def createButton(self,direction,img):
    #     button = tk.Button()
    #     button["image"] = img
    #     button["command"] = self.onClick(direction)
    #     return button
    #===========================================     
    
       
root = tk.Tk()
app = Window(master=root)
app.mainloop()