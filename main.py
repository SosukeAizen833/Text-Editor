# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:18:56 2021

@author: Space
"""
#%%
from tkinter import *
import tkinter.filedialog as filedialog

#%%
root = Tk("Text Editor")
text=Text(root)
text.grid()

#%%
def saveas():
    t = text.get("1.0","end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation,'w+')
    file1.write(t)
    file1.close()
button=Button(root, text="Save", command=saveas)
button.grid()

#%%
def FontHelvetica():
    text.config(font = "Helvetica")

def FontCourier():
    text.config(font = "Courier")
#%%
font = Menubutton(root,text="Font")
font.grid()

font.menu = Menu(font,tearoff =0)
font["menu"] = font.menu

helvetica = IntVar()
arial = IntVar()
times = IntVar()
Courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
command=FontHelvetica) 

root.mainloop()

