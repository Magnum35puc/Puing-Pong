import tkinter as tk
import datetime
from tkinter import ttk
import time
#from weatherGetter import getWeather ##TODO
from horoscopeGetter import getMyHoro

LARGE_FONT = ("arial", 30)
TIME_FONT = ("arial", 40)
WEATHER_FONT = ("arial", 20)

NWTEXT = "Date"
NETEXT = getMyHoro()
SWTEXT = ""#getWeather()
SETEXT = "News"

def getHM():
    HM = time.strftime("%H : %M :")
    return HM

def getS():
    S = time.strftime("%S")
    return S

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

        #### TIME

        time_frame = tk.Frame(self, bg="black")
        time_frame.grid(row=0, column=1, sticky="n", pady=50)
        
        self.HM = tk.Label(time_frame, text=getHM(), fg="white", bg="black", font=TIME_FONT)
        self.HM.grid(row=0, column=0, pady=10, sticky='nwe')

        self.S = tk.Label(time_frame, text=getS(), fg="white", bg="black", font=TIME_FONT)
        self.S.grid(row=0, column=1, pady=10, sticky='nwe')

        #### FOUR CORNERS

        self.NW = tk.Label(self, text = NWTEXT, fg = "white", bg = "black", font = LARGE_FONT)
        self.NW.grid(row = 0, column = 0, padx=20, pady=10, sticky = 'nw')

        self.NE = tk.Label(self, text = NETEXT, fg = "white", bg = "black", font = LARGE_FONT)
        self.NE.grid(row = 0, column = 2, padx=20, pady=10, sticky = 'ne')

        self.SW = tk.Label(self, text = SWTEXT, fg = "white", bg = "black", font = WEATHER_FONT)
        self.SW.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = 'sw')

        self.SE = tk.Label(self, text = SETEXT, fg = "white", bg = "black", font = LARGE_FONT)
        self.SE.grid(row = 1, column = 2, padx = 20, pady = 10, sticky = 'se')

        self.update_clock()

    def update_clock(self):
        HM = getHM()
        S = getS()
        self.HM.configure(text=HM)
        self.S.configure(text=S)
        self.root.after(1000, self.update_clock)


app = Main()
app.geometry("1000x1280")
app.mainloop()
