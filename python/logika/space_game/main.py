from fade import fading
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from scenes import Menu
from pygame import *
from sys import *

# Initialization
init()

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Space Rush")
clock = time.Clock()

current_scene = Menu()
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if not fading:
            current_scene.handle_event(e)

    if not fading:
        current_scene.update()
        current_scene.draw(screen)

        if current_scene.next_scene != current_scene:
            current_scene = current_scene.next_scene

    display.flip() 
    clock.tick(FPS)

quit()