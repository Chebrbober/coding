import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game
from fade import fade_out

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 60)
        self.next_scene = self
        self.button_rect = pygame.Rect(300, 250, 200, 60)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                fade_out(pygame.display.get_surface())  # затемнение
                self.next_scene = Game()

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((30, 30, 30))
        pygame.draw.rect(surface, (100, 200, 100), self.button_rect)
        text = self.font.render("Играть", True, (255, 255, 255))
        surface.blit(text, (self.button_rect.x + 40, self.button_rect.y + 10))
