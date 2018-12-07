import tkinter

master = tkinter.Tk()

master.configure(background='SteelBlue1')
master.columnconfigure(0, weight=1) # make the column 1 expand when the window is resized
nb_of_columns = 2 # to be replaced by the relevant number
titlelabel = tkinter.Label(master, text="my Title", fg="blue4", bg ="gray80")
titlelabel.grid(row=0, column=0, sticky='ew', columnspan=nb_of_columns) # sticky='ew' expands the label horizontally

master.geometry('200x200')
master.mainloop()
