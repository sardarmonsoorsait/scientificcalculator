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

calc = Frame(root,bg="#3a5872")
calc.grid(pady=20,padx=20)

txtDisplay = Entry(calc,font=('arial',20,'bold'),bg='#b6d1c2',width=23,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=7,pady=0)
txtDisplay.insert(0,'0')
Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=1,column=0,pady=10)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=1,column=1,pady=10)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=1,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=1,column=3,pady=10)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=1,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=1,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=1,column=6,pady=10)

Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=2,column=0,pady=10)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=2,column=1,pady=10)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=2,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=2,column=3)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=2,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=2,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=2,column=6,pady=10)

Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=3,column=0,pady=10)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=3,column=1,pady=10)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=3,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=3,column=3,pady=10)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=3,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=3,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=3,column=6,pady=10)

Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=4,column=0,pady=10)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=4,column=1,pady=10)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=4,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=4,column=3,pady=10)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=4,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=4,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=4,column=6,pady=10)

root.mainloop()


                   
                   
                   