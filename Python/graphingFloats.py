import decimal
from tkinter import *
minimum = input("please enter min value: ")
maximum = input("please enter max value: ")
Width = abs(int(minimum)) + abs(int(maximum))
master = Tk()
w = Canvas(master, width=Width, height=200  )
w.pack()

xcoord = [x / 100.0 for x in range((10 * int(minimum)), (10 * int(maximum)))]
ycoord = []
for i in xcoord:
    ycoord.append(i ** 2)

print(xcoord)
print(ycoord)

xcoord = [(i+(Width / 2)) for i in xcoord]
ycoord = [((Width/2) - i) for i in ycoord]

idx = 0
while(idx < ((Width * 2) - 1)):
    x1val = xcoord[idx]
    y1val = ycoord[idx]
    x2val = xcoord[(idx) + 1]
    y2val = ycoord[(idx) + 1]
    w.create_line(x1val, y1val, x2val, y2val, width=1)
    idx = idx + 1
mainloop()