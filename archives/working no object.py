import tkinter as tk
from tkinter.font import Font


class MainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background = "black")
        time_frame = tk.Frame(self)
        time_frame.grid(row=0, column=1)
        big_font = Font(family='Helvetica', size=33, weight='bold')
        small_font = Font(family='Helvetica', size=12, weight='bold')
        HM = tk.Label(time_frame, text="{} :".format(getHM()), fg="white", bg="black", font=big_font)
        HM.grid(row=0, column=0, pady=10)

        S = tk.Label(time_frame, text=getS(), fg="white", bg="black", font=small_font)
        S.grid(row=0, column=1, pady=10, sticky='s')

root = tk.Tk()

def getHM():
    return("10 : 00")

def getS():
    return("34")

MainPage(root).grid(row=0, column=0)
root.mainloop()
