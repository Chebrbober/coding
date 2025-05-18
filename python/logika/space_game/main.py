from fade import fading
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from menu import Menu, Button
#from game import Game
from pygame import *
from sys import *

# Initialization
init()
mixer.init()

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Space Rush")
clock = time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

move_right = False
move_left = False
move_up = False
move_down = False

state = "game"
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if not fading:
            pass
        #current_scene.handle_event(event)

    #current_scene.update()
    #current_scene.draw(screen)

    #if current_scene.next_scene != current_scene:
    #    current_scene = current_scene.next_scene  # Переход на другую сцену

    display.flip()
    clock.tick(FPS)

quit()