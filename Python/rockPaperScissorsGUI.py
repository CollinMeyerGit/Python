import tkinter as tk
from tkinter import *
import random
def play(playerPick):
    pick = random.randint(0,2)
    if pick == 0:
        if playerPick == 0:
            var.set("TIE")
        elif playerPick == 1:
            var.set("PLAYER WINS")
        elif playerPick == 2:
            var.set("COMPUTER WINS")
    if pick == 1:
        if playerPick == 0:
            var.set("COMPUTER WINS")
        elif playerPick == 1:
            var.set("ITS A TIE")
        elif playerPick == 2:
            var.set("PLAYER WINS")
    if pick == 2:
        if playerPick == 0:
            var.set("PLAYER WINS")
        elif playerPick == 1:
            var.set("COMPUTER WINS")
        elif playerPick == 2:
            var.set("ITS A TIE")
window = tk.Tk()
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 2):
        frame = tk.Frame(
            master=window,
            relief=tk.FLAT,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
rockButton = tk.Button(text="ROCK", command=lambda: play(0))
rockButton.grid(row=1, column=0)
paperButton = tk.Button(text="PAPER", command=lambda: play(1))
paperButton.grid(row=1, column=1)
scissorsButton = tk.Button(text="SCISSORS", command=lambda: play(2))
scissorsButton.grid(row=1, column=2)
var = StringVar()
resultLabel = tk.Label(textvariable=var)
resultLabel.grid(row=3, column=1)
window.mainloop()
