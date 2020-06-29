#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:38:32 2020

@author: smsait
"""

from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific calculator")
root.configure(bg="#3a5872")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid(pady=20,padx=20)

txtDisplay = Entry(calc,font=('arial',20,'bold'),bg='#b6d1c2',width=23,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=1,pady=0)
txtDisplay.insert(0,'0')
root.mainloop()


                   
                   
                   