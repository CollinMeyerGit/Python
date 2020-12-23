#This program uses TKinter to illustrate the graph of a cartesian function.
#It does this by first building X and Y coordinate lists
#Then it builds many 1 wide lines to create a very good estimate of a curve

#Collin Meyer 12/22/2020

from tkinter import *
master = Tk()
w = Canvas(master, width=800, height=800)
w.pack()
    #BUILDING X AND Y LISTS
x = []
y = []
var = -400
while(var < 400):
    x.append(var)
    var = (var + 1)
for i in x:
    y.append(i ** 2) # This is the where the function goes
x = [(i+400) for i in x]
y = [(400-i) for i in y]
var = 0
    #DRAWING THE LINES
while(var < 799):
    xval = x[var]
    yval = y[var]
    x2val = x[var+1]
    y2val = y[var+1]
    w.create_line(xval, yval, x2val, y2val, width=3)
    var = (var + 1)
    #AXIS LINES
w.create_line(400, 0, 400, 800)
w.create_line(0, 400, 800, 400)
mainloop()