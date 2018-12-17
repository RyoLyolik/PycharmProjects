import tkinter
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=300, width=600)
canvas.create_line((0, 0), (600, 600), fill='red')
canvas.pack()
master.mainloop()