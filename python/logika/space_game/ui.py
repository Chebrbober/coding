from pygame import *

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