# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:50:45 2023

@author: james
"""

import tkinter as tk
import tkinter .messagebox
window = tk.Tk()
  
window.title("我的第一個GUI程式")  
label = tk.Label(window,text="我的GUI",bg="#05A",fg="#5FC")
window.geometry('300x300')
label.pack()
entry = tk.Entry(window,width = 20)
entry.pack()
def clickMe():
    tkinter.messagebox.showinfo(title='提示' ,message='好痛')
button = tk.Button(window,text = "按鈕",command = clickMe)
button.pack()
window.mainloop()

