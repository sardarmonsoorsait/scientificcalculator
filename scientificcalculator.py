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

#----------------------------------------------------------------------------------------------------------------------------------------
class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()
        
    
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
Button(calc_1,text="7",command=lambda:added_value.numberEnter(7),width=4,height=2,font="helvetica 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=0,pady=10,padx=5)
Button(calc_1,text="8",command=lambda:added_value.numberEnter(8),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=1,pady=10,padx=5)
Button(calc_1,text="9",command=lambda:added_value.numberEnter(9),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=2,pady=10,padx=5)
Button(calc_1,text="+",command=lambda:added_value.numberEnter(7),width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=0,column=3,pady=10,padx=5)
       
       
Button(calc_1,text="4",command=lambda:added_value.numberEnter(4),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=0,pady=10,padx=5)
Button(calc_1,text="5",command=lambda:added_value.numberEnter(5),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=1,pady=10,padx=5)
Button(calc_1,text="6",command=lambda:added_value.numberEnter(6),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=2,pady=10,padx=5)
Button(calc_1,text="-",command=lambda:added_value.numberEnter(7),width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=1,column=3,pady=10,padx=5)       

       
Button(calc_1,text="1",command=lambda:added_value.numberEnter(1),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=0,pady=10,padx=5)
Button(calc_1,text="2",command=lambda:added_value.numberEnter(2),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=1,pady=10,padx=5)
Button(calc_1,text="3",command=lambda:added_value.numberEnter(3),width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=2,pady=10,padx=5)       
Button(calc_1,text="*",command=lambda:added_value.numberEnter(7),width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=2,column=3,pady=10,padx=5)
       
Button(calc_1,text="0",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=0,pady=10,padx=5)
Button(calc_1,text=".",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=1,pady=10,padx=5)
Button(calc_1,text="+/-",width=4,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=2,pady=10,padx=5)       
Button(calc_1,text="/",width=5,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=3,column=3,pady=10,padx=5)
Button(calc_1,text="clear",width=8,height=2,font="arial 8 bold",bd=1,bg="#d86672",fg="#aaa",highlightbackground="#3b0702",highlightcolor="#3b0702",highlightthickness=2).grid(row=4,column=0,columnspan=2,pady=10,padx=5) 
Button(calc_1,text="=",width=8,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa",highlightbackground="#023b1e",highlightcolor="#023b1e",highlightthickness=2).grid(row=4,column=2,pady=10,columnspan=2,padx=5)      
#Button(calc,text="c",width=3,height=2,font="arial 8 bold",bd=1,bg="#2b4753",fg="#aaa").grid(row=5,column=5,padx=5)"""
root.mainloop()



                   
                   
                   