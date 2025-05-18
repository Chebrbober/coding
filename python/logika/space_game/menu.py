from pygame import *
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game
from fade import fade_out
from assets import (
    play_button_none,
    play_button_hovered,
    play_button_pressed,
    exit_button_none,
    exit_button_hovered,
    exit_button_pressed,
    bg,
)


class Button:
    def __init__(self, x, y, images):  # images = [normal, hovered, pressed]
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.clicked = False
        self._pressed = False

    def update(self, mouse_pos, mouse_buttons):
        if self.rect.collidepoint(mouse_pos):
            if mouse_buttons[0]:
                self.image = self.images[2]
                self._pressed = True
            elif self._pressed:
                self.clicked = True
                self._pressed = False
            else:
                self.image = self.images[1]
        else:
            self.image = self.images[0]
            self._pressed = False
            self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def was_clicked(self):
        return self.clicked
class Menu:
    def __init__(self):
        self.next_scene = self
        self.font = font.SysFont(None, 60)

        self.play_button = Button(400, 300, [play_button_none, play_button_hovered, play_button_pressed])
        self.exit_button = Button(400, 400, [exit_button_none, exit_button_hovered, exit_button_pressed])

    def handle_event(self, event):
        pass  # не нужно — логика в update

    def update(self):
        mouse_pos = mouse.get_pos()
        mouse_buttons = mouse.get_pressed()

        self.play_button.update(mouse_pos, mouse_buttons)
        self.exit_button.update(mouse_pos, mouse_buttons)

        if self.play_button.was_clicked():
            fade_out(display.get_surface())
            self.next_scene = Game()

        if self.exit_button.was_clicked():
            quit()

    def draw(self, surface):
        surface.blit(bg, (0, 0))
        self.play_button.draw(surface)
        self.exit_button.draw(surface)