from pygame import *

def draw_fade_overlay(surface, current_alpha):
    """Рисует затемняющий или проявляющийся прямоугольник с заданной прозрачностью."""
    overlay = Surface(surface.get_size(), SRCALPHA) # SRCALPHA для прозрачности
    overlay.fill((0, 0, 0, current_alpha)) # Alpha в последнем параметре
    surface.blit(overlay, (0, 0))