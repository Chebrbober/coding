from pygame import *

def load_image(path, scale=None):
    img = image.load(path)
    if scale:
        img = transform.scale(img, scale)
    return img

# Меню
play_button_none = load_image("images/play_0.png")
play_button_hovered = load_image("images/play_1.png")
play_button_pressed = load_image("images/play_2.png")

exit_button_none = load_image("images/exit_0.png")
exit_button_hovered = load_image("images/exit_1.png")
exit_button_pressed = load_image("images/exit_2.png")

bg = load_image("images/bg.png")

# Гра
