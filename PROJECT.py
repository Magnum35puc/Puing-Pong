# coding=utf-8

import tkinter as tk
import datetime
from tkinter import ttk
import time
from weatherAPI import getWeather
from horoscopeGetter import getMyHoro
import newsAPI
from numpy import sin
import math

def getDate():
    return DAYS[datetime.datetime.now().weekday()] + datetime.datetime.today().strftime(" %d ") + MONTHS[int(datetime.datetime.today().strftime("%m"))]

LARGE_FONT = ("arial", 30)
TIME_FONT = ("arial", 50)
SECONDS_FONT = ("arial", 20)
WEATHER_FONT = ("arial", 20)
NEWS_FONT = ("arial", 16)
DAYS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
MONTHS = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

NWTEXT = getDate()
NETEXT = getMyHoro()
SWTEXT = getWeather()
SETEXT = newsAPI.getNews()

def getHM():
    HM = time.strftime("%H : %M")
    return HM

def getS():
    S = time.strftime(" : %S")
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
        
        self.HM = tk.Label(time_frame, text=getHM(), fg="white", bg="black", font=TIME_FONT, anchor = "s", justify = "center")
        self.HM.grid(row=0, column=0, pady=10, sticky='nwe')

        self.S = tk.Label(time_frame, text=getS(), fg="white", bg="black", font=SECONDS_FONT, anchor = "s")
        self.S.grid(row=0, column=1, pady=10, sticky='nwe')

        #### FOUR CORNERS

        self.NW = tk.Label(self, text = NWTEXT, fg = "white", bg = "black", font = LARGE_FONT, justify="left")
        self.NW.grid(row = 0, column = 0, padx=20, pady=10, sticky = 'nw')

        self.NE = tk.Label(self, text = NETEXT, fg = "white", bg = "black", font = LARGE_FONT, anchor = 'e', justify="left")
        self.NE.grid(row = 0, column = 2, padx=20, pady=10, sticky = 'ne')

        self.SW = tk.Label(self, text = SWTEXT, fg = "white", bg = "black", font = WEATHER_FONT, anchor = 'w', justify="left")
        self.SW.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = 'sw')

        self.SE = tk.Label(self, text = SETEXT, fg = "#FFFFFF", bg = "black", font = NEWS_FONT, anchor = 'w', justify="left")
        self.SE.grid(row = 1, column = 2, columnspan=2, padx = 20, pady = 10, sticky = 'se')

        self.update_clock()
        self.update_news()
        
        global a
        a = datetime.datetime.now()
        self.update_news_color()

    def update_clock(self):
        HM = getHM()
        S = getS()
        
        self.HM.configure(text=HM)
        self.S.configure(text=S)
        self.root.after(1000, self.update_clock)

        
    def update_news(self):
        news = newsAPI.getNews()
        
        self.SE.configure(text=news)
        self.root.after(10000, self.update_news)

    def update_news_color(self):
        global a
        b = datetime.datetime.now()
        delta = b - a

        counter = int(round(255* (sin(delta.total_seconds()/10*math.pi)*3**2)))
        if counter > 255:
            counter = 255
        if counter < 0:
            counter = -counter
        col = '#{:02x}{:02x}{:02x}'.format(counter,counter,counter)
        self.SE.configure(fg = col)
        self.root.after(50, self.update_news_color)

app = Main()
app.geometry("1000x1280")
app.mainloop()










