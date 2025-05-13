from pygame import *
from sys import *

# Initialization
init()
mixer.init()

screen_width = 500
screen_height = 800
screen = display.set_mode((screen_width, screen_height))
display.set_caption("Space Rush")
clock = time.Clock()

move_right = False
move_left = False
move_up = False
move_down = False

def something():
    pass

destroyed = False
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    display.update()
    clock.tick(60)