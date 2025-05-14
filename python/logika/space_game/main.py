from settings import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
#from menu import Menu
#from game import Game
from pygame import *
from sys import *

# Initialization
init()
mixer.init()


screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Space Rush")
clock = time.Clock()
fps = 60

move_right = False
move_left = False
move_up = False
move_down = False

class GameSprite(sprite.Sprite):
    pass

def something():
    pass

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        #current_scene.handle_event(event)

    #current_scene.update()
    #current_scene.draw(screen)

    #if current_scene.next_scene != current_scene:
    #    current_scene = current_scene.next_scene  # Переход на другую сцену

    display.flip()
    clock.tick(FPS)

quit()