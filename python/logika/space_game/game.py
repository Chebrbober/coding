from pygame import *
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self):
        #self.image = player_img
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.speed = 5

    def handle_keys(self, keys):
        if keys[K_w]: self.rect.y -= self.speed
        if keys[K_s]: self.rect.y += self.speed
        if keys[K_a]: self.rect.x -= self.speed
        if keys[K_d]: self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Game:
    def __init__(self):
        self.player = Player()
        self.next_scene = self

    def handle_event(self, event):
        pass  # стрельба и пауза потом

    def update(self):
        keys = key.get_pressed()
        self.player.handle_keys(keys)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.player.draw(surface)
