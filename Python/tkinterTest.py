import tkinter as tk
import tkmessagebox

top = tk.Tk()

def helloCallBack():
   tkLabel.showinfo( "Hello Python", "Hello World")

B = tk.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()