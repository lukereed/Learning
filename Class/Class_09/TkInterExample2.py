# Luke Reed
# TkInterExample2.py
# 03/17/2016
# a script for introducing to making new windows and interactive programs/GUI's

import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
	tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
