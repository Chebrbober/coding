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
        if not current_scene.is_fading:
            current_scene.handle_event(e)

    current_scene.update()

    if current_scene.next_scene != current_scene:
        current_scene = current_scene.next_scene

    screen.fill((0, 0, 0))
    current_scene.draw(screen)

    display.flip() 
    clock.tick(FPS)

quit()