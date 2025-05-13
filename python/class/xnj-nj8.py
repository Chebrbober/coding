from tkinter import *
root = Tk()
root.geometry("850x400")
c = Canvas (width=850, height=400, bg="white")
c.pack()
c.create_line(30, 40, 150, 40, 80, 200, 30, 40, \
fill="green", dash=(10,5), width=2, arrow='first')
c.create_rectangle (250, 40, 400, 300, width=4, \
    outline="blue", fill="yellow")
c.create_oval (500, 40, 800, 300, width=8, \
    dash=8, outline="red", fill="blue")
root.mainloop()
