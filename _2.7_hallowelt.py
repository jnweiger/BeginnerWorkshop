import Tkinter 

from Tkinter import *


tk = Tkinter.Tk()


frame = Tkinter.Frame(tk, relief = RIDGE, borderwidth = 2)
frame.pack(fill = BOTH, expand = 1)


label = Tkinter.Label(frame, text = "Hallo, Welt!")
label.pack(fill = X, expand = 1)


button = Tkinter.Button(frame, text = "Exit", 
          command = tk.destroy)
button.pack(side = BOTTOM, padx = 4, pady = 4)


Tkinter.mainloop()
