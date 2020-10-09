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
    frame = tk.Frame(bg="#3E4149")
    window.minsize(height, width)
    window.configure(bg="#3E4149")

    frame.pack()
    label1 = tk.Label(frame, width=40, text="Enter website to extract HAR file", bg="#3E4149").grid(row=0, column=0, columnspan=10)
    submit = tk.Button(frame, text="Search", highlightbackground='#3E4149', width=10).grid(row=1, column=0)
    entry = tk.Entry(frame, width=50, bg="#3E4149", highlightbackground="#3E4149").grid(row=1, column=1, columnspan=9)


    scrollbar = Scrollbar(frame, orient="vertical", bg="#3E4149").grid(row=2, column=1)
    listbox = Listbox(frame, yscrollcommand=scrollbar, width=80, bg="#3E4149").grid(row=2, column=0, columnspan=10)

    profileLabel = tk.Label(frame, text="Profiles", bg="#3E4149").grid(row=3,column=6, columnspan=2)
    profiles = Listbox(frame, yscrollcommand=scrollbar, width=40, bg="#3E4149").grid(row=4,column=5, columnspan=4)

    #start = tk.Button(player, text="Start",command=lambda: countdowner(listbox.curselection(), timeleft, currsong, window), width=15)
    window.mainloop()
