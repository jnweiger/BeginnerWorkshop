try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

tk = tkinter.Tk()


frame = tkinter.Frame(tk, relief=tkinter.RIDGE, borderwidth=2)
frame.pack(fill=tkinter.BOTH, expand=1)


label = tkinter.Label(frame, text="Hallo, Welt!")
label.pack(fill=tkinter.X, expand=1)


button = tkinter.Button(frame, text="Exit",
          command=tk.destroy)
button.pack(side=tkinter.BOTTOM, padx=4, pady=4)


tkinter.mainloop()
