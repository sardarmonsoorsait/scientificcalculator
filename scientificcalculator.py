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
root.configure(bg="#3a5872",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=4)
root.resizable(width=False,height=False)
root.geometry("325x625+0+0")

calc = Frame(root,bg="#3a5872")
calc.grid(pady=20,padx=20)

txtDisplay = Entry(calc,font=('arial',30,'bold'),bg='#b6d1c2',width=10,justify=RIGHT,highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2)
txtDisplay.grid(row=0,column=0,columnspan=7,ipady=10)
txtDisplay.insert(0,'0')
Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#0a2618",
                             highlightcolor="#0a2618",
                             highlightthickness=2).grid(row=1,column=0,pady=10,padx=0)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=1,pady=10,)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=3,pady=10)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=6,pady=10)

Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=0,pady=10)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=1,pady=10)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=3)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=6,pady=10)

Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=0,pady=10)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=1,pady=10)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=3,pady=10)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=6,pady=10)

Button(calc,text="2nd",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=0,pady=10)
Button(calc,text="(",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=1,pady=10)
Button(calc,text=")",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=2,pady=10)
Button(calc,text="%",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=3,pady=10)
Button(calc,text="1/x",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=4,pady=10)
Button(calc,text="x^2",width=1,height=1,font=" arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=5,pady=10)
Button(calc,text="x^3",width=1,height="1",font="arial 7 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=6,pady=10)

calc_1=Frame(root,bg="#3a5880")
calc_1.grid()
Button(calc_1,text="7",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=0,pady=10,padx=5)
Button(calc_1,text="8",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=1,pady=10,padx=5)
Button(calc_1,text="9",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=2,pady=10,padx=5)
Button(calc_1,text="+",width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=3,pady=10,padx=5)
       
       
Button(calc_1,text="4",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=0,pady=10,padx=5)
Button(calc_1,text="5",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=1,pady=10,padx=5)
Button(calc_1,text="6",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=2,pady=10,padx=5)
Button(calc_1,text="-",width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=3,pady=10,padx=5)       

       
Button(calc_1,text="1",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=0,pady=10,padx=5)
Button(calc_1,text="2",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=1,pady=10,padx=5)
Button(calc_1,text="3",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=2,pady=10,padx=5)       
Button(calc_1,text="*",width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=3,pady=10,padx=5)
       
Button(calc_1,text="0",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=0,pady=10,padx=5)
Button(calc_1,text=".",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=1,pady=10,padx=5)
Button(calc_1,text="+/-",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=2,pady=10,padx=5)       
Button(calc_1,text="/",width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=3,pady=10,padx=5)
Button(calc_1,text="clear",width=8,height=2,font="arial 8 bold",bd=1,bg="#d86672",fg="#aaa",highlightbackground="#3b0702",highlightcolor="#3b0702",highlightthickness=2).grid(row=4,column=0,columnspan=2,pady=10,padx=5) 
Button(calc_1,text="=",width=8,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=2,pady=10,columnspan=2,padx=5)      
#Button(calc,text="c",width=3,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=5,column=5,padx=5)"""
root.mainloop()



                   
                   
                   