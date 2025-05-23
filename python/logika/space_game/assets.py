from pygame import *

def load_image(path, scale=None):
    img = image.load(path)
    if scale:
        img = transform.scale(img, scale)
    return img

# Меню
play_button_none = load_image("images/play_0.png", (217, 105))
play_button_hovered = load_image("images/play_1.png", (217, 105))
play_button_pressed = load_image("images/play_2.png", (217, 105))

exit_button_none = load_image("images/exit_0.png", (72, 72))
exit_button_hovered = load_image("images/exit_1.png", (72, 72))
exit_button_pressed = load_image("images/exit_2.png", (72, 72))

levelone_button_none = load_image("images/lvlone_0.png", (75, 75))
levelone_button_hovered = load_image("images/lvlone_1.png", (75, 75))
levelone_button_pressed = load_image("images/lvlone_2.png", (75, 75))

leveltwo_button_none = load_image("images/lvltwo_0.png", (75, 75))
leveltwo_button_hovered = load_image("images/lvltwo_1.png", (75, 75))
leveltwo_button_pressed = load_image("images/lvltwo_2.png", (75, 75))

back_none = load_image("images/back_0.png", (72, 72))
back_hovered = load_image("images/back_1.png", (72, 72))
back_pressed = load_image("images/back_2.png", (72, 72))

bg = load_image("images/bg.png", (600, 900))
board_name = load_image("images/board.png", (450, 350))
board_lvl = load_image("images/board_lvl.png", (375, 200))
game_name = load_image("images/game_name.png", (300, 225))
lvl_name = load_image("images/lvl_name.png", (300, 100))

menu_music = menu_music = "audio/menu_theme.mp3"
#level_music = "music/level_theme.mp3"

# Гра
