import tkinter as tk
import datetime
from tkinter import ttk
import time

LARGE_FONT = ("arial", 20)

NWTEXT = "weather"
NETEXT = ""

def getTime():
    timetxt = time.strftime("%H:%M:%S")
    return timetxt

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1)
        self.configure(background='black')

        main_container = tk.Frame(self)
        main_container.grid(column=0, row=0, sticky = "nsew")
        main_container.grid_rowconfigure(0, weight = 1)
        main_container.grid_columnconfigure(0, weight = 1)

        main_container.configure(background="black")

        self.frames = {}

        for fr in (MainPage,):
            frame = fr(main_container, self)
            self.frames[fr] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(MainPage)

    def show_frame(self, pointer):
        frame = self.frames[pointer]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background = "black")
        self.root = parent
        
        self.columnconfigure(0, weight = 1, uniform = "x")
        self.columnconfigure(1, weight = 1, uniform = "x")
        self.columnconfigure(2, weight = 1, uniform = "x")
        self.rowconfigure(0, weight = 1, uniform = "x")
        self.rowconfigure(1, weight = 1, uniform = "x")

        self.label = tk.Label(self, text = NWTEXT, fg = "white", bg = "black", font = LARGE_FONT)
        self.label.grid(row = 0, column = 0, padx=20, pady=10, sticky = 'nw')

        self.time = tk.Label(self, text = getTime(), fg = "white", bg = "black", font = LARGE_FONT)
        self.time.grid(row = 0, column = 1, pady=10, sticky = 'nwe')

        self.label = tk.Label(self, text = NETEXT, fg = "white", bg = "black", font = LARGE_FONT)
        self.label.grid(row = 0, column = 2, padx=20, pady=10, sticky = 'ne')

        self.label2 = tk.Label(self, text = "News", fg = "white", bg = "black", font = LARGE_FONT)
        self.label2.grid(row = 1, column = 0, pady = 10, sticky = 'sw')

        self.update_clock()

    def update_clock(self):
        now = getTime()
        self.time.configure(text=now)
        self.root.after(1000, self.update_clock)


app = Main()
app.geometry("1000x1280")
app.mainloop()
