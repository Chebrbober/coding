from pygame import *

def fade_out(surface, speed=10):
    fade = Surface(surface.get_size())
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        surface.blit(fade, (0, 0))
        display.update()
        time.delay(10)