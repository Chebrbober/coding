from pygame import *

fading = False

def fade_out(surface, speed=5):
    fading = True
    fade = Surface(surface.get_size())
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        surface.blit(fade, (0, 0))
        display.update()
        time.delay(10)