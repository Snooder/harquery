import os
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
from tkinter import filedialog
from tkinter import Scrollbar
from tkinter import Frame
import importlib


height = 400
width = 600
if __name__ == '__main__':
    window = tk.Tk()
    frame = tk.Frame()
    window.minsize(height, width)

    frame.pack()
    label1 = tk.Label(frame, width=40, text="Enter website to extract HAR file")
    label1.pack()

    entry = tk.Entry(frame, width=50, bg="white", fg="black")
    entry.pack(side=tk.RIGHT)

    folder = tk.Button(frame, text="Search", width=10)
    folder.pack(side=tk.RIGHT)

    seperator = Frame()
    seperator.pack()
    scrollbar = Scrollbar(seperator, orient="vertical")
    listbox = Listbox(seperator, yscrollcommand=scrollbar.set, width=80)
    scrollbar.config(command=listbox.yview)
    listbox.pack(side=tk.LEFT)
    scrollbar.pack(side=tk.LEFT, fill=tk.X)

    player = Frame()
    player.pack()
    currsong = tk.Label(player, text="")
    currsong.pack(side=tk.TOP)
    timeleftlabel = tk.Label(player, text="Time Left: ")
    timeleftlabel.pack(side=tk.LEFT)
    timeleft = tk.Label(player, text="")
    timeleft.pack(side=tk.LEFT)
    start = tk.Button(player, text="Start",command=lambda: countdowner(listbox.curselection(), timeleft, currsong, window), width=15)
    start.pack(side=tk.LEFT)
    stop = tk.Button(player, text="Stop",command=lambda: stopTimer(window), width=15)
    stop.pack(side=tk.LEFT)

    window.mainloop()
