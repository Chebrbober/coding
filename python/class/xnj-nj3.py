from tkinter import *
root = Tk()
root.geometry("350x300")

c= Canvas (width=350, height=300)
c.pack()
c.create_line(250, 220, 200,170, \
              190, 170, 185, 175, \
              190, 180, 190, 200, \
              200, 210, 220, 215, \
              235, 215, 250, 220, \
              width=4, fill="green")
root.mainloop()
