import tkinter 

from tkinter.constants import *


tk = tkinter.Tk()


frame = tkinter.Frame(tk, relief = RIDGE, borderwidth = 2)
frame.pack(fill = BOTH, expand = 1)


label = tkinter.Label(frame, text = "Hallo, Welt!")
label.pack(fill = X, expand = 1)


button = tkinter.Button(frame, text = "Exit", 
          command = tk.destroy)
button.pack(side = BOTTOM, padx = 4, pady = 4)


tkinter.mainloop()
