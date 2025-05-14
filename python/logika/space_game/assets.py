from pygame import *
from settings import PLAYER_IMAGE

def load_image(path, scale=None):
    img = image.load(path).convert_alpha()
    if scale:
        img = transform.scale(img, scale)
    return img

# Заранее загружаем изображения
player_img = load_image(PLAYER_IMAGE, (64, 64))
# enemy_img = ...
# bullet_img = ...
