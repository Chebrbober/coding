from tkinter import *
def triangle(x, y, a):
    c.create_line(x, y, x+a, y, width=5, fill='red')
    c.create_line(x+a,y, x+a//2,y+100, width=5,\
            fill='red')
    c.create_line(x+a//2,y+100, x, y, width=5,\
            fill='red')
root = Tk()
root.geometry("600x600")
c=Canvas (width=600, height=600)
c.pack()
triangle (100, 100, 200)
triangle (200, 400, 300)
root.mainloop()
