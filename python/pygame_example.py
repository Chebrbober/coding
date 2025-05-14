from pygame import *
from sys import *

# Initialization
init()
mixer.init()

screen_width = 600
screen_height = 900
screen = display.set_mode((screen_width, screen_height))
display.set_caption("Space Rush")
clock = time.Clock()
fps = 60

play = True
while not destroyed:
    mouse_pos = mouse.get_pos()
    events = event.get()
    for e in events:
        if e.type == QUIT:
            destroyed = False
    display.update()
    clock.tick(fps)

quit()