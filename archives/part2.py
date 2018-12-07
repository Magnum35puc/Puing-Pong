import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGE_FONT = ("Verdana", 12)

class SmartMirror(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Smart Mirror")

        self.geometry("1280x720")
        #self.attributes('-fullscreen', True)
        self.configure(background='white')
        self.bind('<Escape>',lambda e: self.destroy())

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        container = tk.Frame(self)
        container.pack(fill="both", expand = True)
        
        container.grid_rowconfigure(1, weight = 1)
        container.grid_columnconfigure(1, weight = 1)

        self.frames = {}

        
        for F in (StartPage,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, pointer):
        frame = self.frames[pointer]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        
        label = tk.Label(self, text = "TEST 1", font=LARGE_FONT, fg = "white", bg="black", anchor=NW)
        label.grid(row = 0, column = 0)

        label2 = tk.Label(self, text = "TEST 2", font=LARGE_FONT, fg = "white", bg="black", anchor=NE)
        label2.grid(row = 1, column = 1)

        self.configure(background='black')

'''
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Hallo", font=LARGE_FONT)
        label.pack(pady=100, padx=100)

        button1 = ttk.Button(self, text="Home",
                            command = lambda : controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page 2",
                            command = lambda : controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "this is the second page", font=LARGE_FONT)
        label.pack(pady=100, padx=100)

        button1 = ttk.Button(self, text="Home",
                            command = lambda : controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command = lambda : controller.show_frame(PageOne))
        button2.pack()'''


app = SmartMirror()
app.mainloop()
